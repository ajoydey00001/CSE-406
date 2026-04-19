rule stringrule_1{
    meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
    strings:
        $config_decr = { 48 89 45 F0 C7 45 EC 08 01 00 00 C7 45 FC 28 00 00 00 EB 31 8B 45 FC 48 63 D0 48 8B 45 F0 48 01 C2 8B 45 FC 48 63 C8 48 8B 45 F0 48 01 C8 0F B6 00 89 C1 8B 45 F8 89 C6 8B 45 FC 01 F0 31 C8 88 02 83 45 FC 01 }
        $export1 = "our_sockets"
        $export2 = "get_our_pids"
        $rafi = "check_is_our_proc_dir"
    condition:
        uint16(0) == 0x457f and all of them
}

rule stringrule_2
{
    meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
    strings:
        $ = "_errno" ascii wide nocase
        $ = "atoi" ascii wide nocase
        $ = "fclose" ascii wide nocase
        $ = "fgets" ascii wide nocase
        $ = "fputs" ascii wide nocase
        $ = "fseek" ascii wide nocase
        $ = "getenv" ascii wide nocase
        $ = "memcpy" ascii wide nocase
        $ = "memset" ascii wide nocase
        $ = "socket" ascii wide nocase
        $ = "sprintf" ascii wide nocase
        $ = "sscanf" ascii wide nocase
        $ = "strcat" nocase
        $ = "strchr" nocase
        $ = "strcmp" fullword
        $ = "strlen" fullword
        $ = "strncmp" fullword
        $ = "strncpy" fullword
        $ = "strstr" fullword
    

    condition:
            {any of them } and not {all of them}
 
}

rule stringrule_3
{
	meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
    strings:
		$0 = {60}
	condition:
		$0
}

rule stringrule_4
{
	meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"

	strings:
		$0 = {FF F5}
		
		$2 = {FF F8}
		$3 = {FF FC}
		$4 = {FF F0}
		
		$9 = {FF F9}
		
		$13 = {FF E3}
		$14 = {FF FE}
		
	condition:
		$0 at entrypoint or $2 or $3 or $4 or $9 or $13 or $14 
}


rule stringrule_5
{
    meta:
        writter="written by Ajoy and Rafi"
        date="02-03-2024"
    strings:
        $a1 = "libutil.so.1" fullword
        $a2 = "librt.so.1"
        $a3 = "libthread.so.0" fullword

        $b1 = "strstr"  nocase
        $b2 = "fputs"   nocase
        $b3 = "opendir" 
        $b4 = "syscall_list"

        $c1 = "antimalware" nocase
        $c2 = "firewall" nocase
    

    condition:
            (1 of ($a*)) and (any of ($b*)) and not (any of ($c*))
 
}



