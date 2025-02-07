#include <string>
#include <iostream>

// Function to convert a hex string to a Base32 string
std::string hexToBase32(const std::string& hexKey) {
    // Define the Base32 encoding table
    const char base32Chars[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";

    // Convert hex to binary
    std::string binaryKey;
    for (char hexChar : hexKey) {
        if (hexChar == '\0') {
            // Handle null character as any other character
            binaryKey.push_back('0');
            binaryKey.push_back('0');
            binaryKey.push_back('0');
            binaryKey.push_back('0');
        } else {
            int hexValue;
            std::sscanf(&hexChar, "%1X", &hexValue);  // Convert hex char to integer
            for (int i = 3; i >= 0; --i) {
                binaryKey.push_back(((hexValue >> i) & 1) ? '1' : '0');
            }
        }
    }

    // Add padding to make the length a multiple of 40 (8 characters)
    while (binaryKey.length() % 40 != 0) {
        binaryKey.push_back('0');
    }

    // Convert binary to Base32
    std::string base32Key;
    for (size_t i = 0; i < binaryKey.length(); i += 5) {
        int index = 0;
        for (size_t j = 0; j < 5; ++j) {
            index = (index << 1) + (binaryKey[i + j] - '0');
        }
        base32Key.push_back(base32Chars[index]);
    }

    size_t  i = base32Key.length() - 1;
    while (base32Key[i] == 'A') {
        base32Key[i] = '=';
        --i;
    }
    std::cout << "Base32: " << base32Key << std::endl;
    return base32Key;
}
