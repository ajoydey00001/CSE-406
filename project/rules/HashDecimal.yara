rule HashDecimal_rule {
    meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
    strings:
        $a = { 89 E5 48 89 7D D8 48 8B 45 D8 0F B6 40 27 0F BE C0 89 45 F8 48 8B }
    condition:
        all of them
}
