import "hash"

import "hash"

rule hash_demo_rule{
    meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
        description="hash test"
    

    condition:
	// substring is "!"#$%&'()*+'-./0123456789:;<=>?@ABCDEFGHIJKLM"
        
        hash.md5(0x000054fb,45) == "e4d4f84ed611c39eba1b2c1eca3a5251"
	or
	hash.sha1(0x000054fb,45) == "08698d0bd72a7c8d6a2a236ac6a38fd1317aa2c7"
}

rule offset{
    meta:
        description = "test"
    strings:
        $name = { 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f 40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d  }
    condition:
        $name at 0x000054fb
}
