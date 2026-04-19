rule ELF_magic
{
	meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
		description = "Detect ELF 64 bit executable based on ELF magic"

	condition:
                //starts with the correct ELF magic bytes and is identified as a 64-bit ELF executable.
                uint32(0) == 0x464c457f and  //This condition checks the first 4 bytes of the file (offset 0) to ensure they match the ELF magic bytes 0x7F 'E' 'L' 'F' represented as 0x464c457f in hexadecimal
		uint8(4) == 0x02  //This condition checks the byte at offset 4 in the file to verify that it corresponds to a 64-bit ELF executable. The value 0x02 indicates that it's a 64-bit ELF executable (ELFCLASS64).
}

