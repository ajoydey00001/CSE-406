import "elf"

rule elf_64
{
    condition:
        elf.machine == elf.EM_X86_64
}
