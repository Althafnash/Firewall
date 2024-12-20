yara_rules = '''
rule DebuggerCheck__PEB : AntiDebug DebuggerCheck {
    meta:
        weight = 1
        Author = "naxonez"
        reference = "https://github.com/naxonez/yaraRules/blob/master/AntiDebugging.yara"
    strings:
        $a = "IsDebugged"
    condition:
        any of them
}

rule DebuggerCheck__PEB : AntiDebug DebuggerCheck {
	meta:
		weight = 1
		Author = "naxonez"
		reference = "https://github.com/naxonez/yaraRules/blob/master/AntiDebugging.yara"
	strings:
		$ ="IsDebugged"
	condition:
		any of them
}

'''