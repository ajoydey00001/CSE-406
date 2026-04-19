

rule math_entropy_4 : info statistics {
	meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
	
	    description = "Low entropy - like plaintext or HTML or sparse data"

	condition:
	//it Returns the entropy for size bytes starting at offset
		math.entropy(0, filesize) >= 4 and
		math.entropy(0, filesize) < 5
}

