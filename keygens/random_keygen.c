/*
 * Using /dev/urandom or /dev/random is generally more secure and
 * 	provides better randomness than using rand() with a time-based seed.
 *
 * Advantages of Using /dev/xrandom:
 * 
 * 	- Cryptographic Security: /dev/xrandom is designed to provide
 * 		cryptographically secure random numbers. It uses environmental
 * 		noise collected from device drivers and other sources to generate
 *		random numbers, making it much harder to predict the output.
 * 
 * 	- Non-Deterministic: Unlike rand(), which is a pseudo-random number
 *		generator (PRNG) that produces a deterministic sequence based on
 *		an initial seed, /dev/xrandom generates non-deterministic random
 *		numbers. This means that even if you read from it multiple times
 *		in quick succession, you will get different values.
 * 
 * 	- Higher Entropy: The randomness quality (entropy) of numbers generated
 *		from /dev/xrandom is significantly higher than that of rand().
 *	  This makes it suitable for applications that require high-quality
 *		randomness, such as cryptographic keys, secure tokens, and other
 *		security-sensitive operations.
 *
 *
 * /dev/urandom or /dev/random:
 * ----------------------------
 *
 * Blocking Behavior: /dev/random is a blocking source of random numbers.
 * This means that if there is not enough entropy (randomness) available
 * 	in the system, reading from /dev/random will block (i.e., wait) until
 * 	sufficient entropy is gathered.
 * This can lead to delays in applications that require random numbers.
 *
 * While it may not provide the same level of entropy as /dev/random,
 * 	/dev/urandom is generally considered secure enough for most applications,
 * 	including cryptographic purposes. 
 */

# include <stdio.h>
# include <fcntl.h>
# include <unistd.h>
# include <stdlib.h>
# include <string.h>

# define DC_KEYCHARSET          "abcdefghijklmnopqrstuvwxyz" \
                                "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                                "0123456789"

# define DC_KEY_SIZE			16

unsigned char *generate_random_based_key(
	const char *charset, size_t strength, int blocking
	) {
	unsigned char *key = malloc((strength + 1) * sizeof(char));
	if (key == NULL) return NULL;

	int charset_length = strlen(charset);

    int fd = open(
		blocking ? "/dev/urandom" : "/dev/random",
		O_RDONLY
		);
    if (fd < 0) return NULL;

    unsigned char random_bytes[strength];
    if (read(fd, random_bytes, strength) != strength) {
        perror("read");
        close(fd);
        exit(EXIT_FAILURE);
    }
    close(fd);

    for (size_t i = 0; i < strength; ++i) {
        int random_index = random_bytes[i] % charset_length;
        key[i] = charset[random_index];
    }
    key[strength] = '\0'; // Null-terminate the string

	return key;
}

 int main()
 {
	unsigned char	*key_blocking = generate_random_based_key(
		DC_KEYCHARSET, DC_KEY_SIZE, 0
		);

	unsigned char	*key_non_blocking = generate_random_based_key(
		DC_KEYCHARSET, DC_KEY_SIZE, 1
		);

	if (!key_blocking || !key_non_blocking) {
		fprintf(stderr, "Failed to generate key.\n");
		return 1;
	}

	printf("Keygen (blocking random):\t%s\n", key_blocking);
	printf("Keygen (non-blocking random):\t%s\n", key_non_blocking);

	free(key_blocking);
	free(key_non_blocking);

	return 0;
 }
