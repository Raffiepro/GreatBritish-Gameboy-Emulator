data = {
	"unprefixed": {
		"0x00": {
			"mnemonic": "NOP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x01": {
			"mnemonic": "LD",
			"bytes": 3,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "BC",
					"immediate": True
				},
				{
					"name": "n16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x02": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "BC",
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x03": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "BC",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x04": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x05": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x06": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x07": {
			"mnemonic": "RLCA",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "0",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x08": {
			"mnemonic": "LD",
			"bytes": 3,
			"cycles": [
				20
			],
			"operands": [
				{
					"name": "a16",
					"bytes": 2,
					"immediate": False
				},
				{
					"name": "SP",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x09": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				},
				{
					"name": "BC",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x0A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "BC",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x0B": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "BC",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x0C": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x0D": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x0E": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x0F": {
			"mnemonic": "RRCA",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "0",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x10": {
			"mnemonic": "STOP",
			"bytes": 2,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x11": {
			"mnemonic": "LD",
			"bytes": 3,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "DE",
					"immediate": True
				},
				{
					"name": "n16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x12": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "DE",
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x13": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "DE",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x14": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x15": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x16": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x17": {
			"mnemonic": "RLA",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "0",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x18": {
			"mnemonic": "JR",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "e8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x19": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				},
				{
					"name": "DE",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x1A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "DE",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x1B": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "DE",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x1C": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x1D": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x1E": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x1F": {
			"mnemonic": "RRA",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "0",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x20": {
			"mnemonic": "JR",
			"bytes": 2,
			"cycles": [
				12,
				8
			],
			"operands": [
				{
					"name": "NZ",
					"immediate": True
				},
				{
					"name": "e8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x21": {
			"mnemonic": "LD",
			"bytes": 3,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				},
				{
					"name": "n16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x22": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"increment": True,
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x23": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x24": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x25": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x26": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x27": {
			"mnemonic": "DAA",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "-",
				"H": "0",
				"C": "C"
			}
		},
		"0x28": {
			"mnemonic": "JR",
			"bytes": 2,
			"cycles": [
				12,
				8
			],
			"operands": [
				{
					"name": "Z",
					"immediate": True
				},
				{
					"name": "e8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x29": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x2A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"increment": True,
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x2B": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x2C": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x2D": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x2E": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x2F": {
			"mnemonic": "CPL",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "1",
				"H": "1",
				"C": "-"
			}
		},
		"0x30": {
			"mnemonic": "JR",
			"bytes": 2,
			"cycles": [
				12,
				8
			],
			"operands": [
				{
					"name": "NC",
					"immediate": True
				},
				{
					"name": "e8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x31": {
			"mnemonic": "LD",
			"bytes": 3,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "SP",
					"immediate": True
				},
				{
					"name": "n16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x32": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"decrement": True,
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x33": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "SP",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x34": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x35": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x36": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x37": {
			"mnemonic": "SCF",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "0",
				"H": "0",
				"C": "1"
			}
		},
		"0x38": {
			"mnemonic": "JR",
			"bytes": 2,
			"cycles": [
				12,
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "e8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x39": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				},
				{
					"name": "SP",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x3A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"decrement": True,
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x3B": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "SP",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x3C": {
			"mnemonic": "INC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "-"
			}
		},
		"0x3D": {
			"mnemonic": "DEC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0x3E": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x3F": {
			"mnemonic": "CCF",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x40": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x41": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x42": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x43": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x44": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x45": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x46": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x47": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x48": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x49": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x4A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x4B": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x4C": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x4D": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x4E": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x4F": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x50": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x51": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x52": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x53": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x54": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x55": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x56": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x57": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x58": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x59": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x5A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x5B": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x5C": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x5D": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x5E": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x5F": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x60": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x61": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x62": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x63": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x64": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x65": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x66": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x67": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x68": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x69": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x6A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x6B": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x6C": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x6D": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x6E": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x6F": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x70": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x71": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x72": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x73": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x74": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x75": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x76": {
			"mnemonic": "HALT",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x77": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x78": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x79": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x7A": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x7B": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x7C": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x7D": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x7E": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x7F": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x80": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x81": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x82": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x83": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x84": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x85": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x86": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x87": {
			"mnemonic": "ADD",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x88": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x89": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x8A": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x8B": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x8C": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x8D": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x8E": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x8F": {
			"mnemonic": "ADC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0x90": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x91": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x92": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x93": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x94": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x95": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x96": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x97": {
			"mnemonic": "SUB",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "1",
				"N": "1",
				"H": "0",
				"C": "0"
			}
		},
		"0x98": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x99": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x9A": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x9B": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x9C": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x9D": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x9E": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0x9F": {
			"mnemonic": "SBC",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "-"
			}
		},
		"0xA0": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA1": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA2": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA3": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA4": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA5": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA6": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA7": {
			"mnemonic": "AND",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xA8": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xA9": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xAA": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xAB": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xAC": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xAD": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xAE": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xAF": {
			"mnemonic": "XOR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "1",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB0": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB1": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB2": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB3": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB4": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB5": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB6": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB7": {
			"mnemonic": "OR",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xB8": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xB9": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xBA": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xBB": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xBC": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xBD": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xBE": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xBF": {
			"mnemonic": "CP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "1",
				"N": "1",
				"H": "0",
				"C": "0"
			}
		},
		"0xC0": {
			"mnemonic": "RET",
			"bytes": 1,
			"cycles": [
				20,
				8
			],
			"operands": [
				{
					"name": "NZ",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC1": {
			"mnemonic": "POP",
			"bytes": 1,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "BC",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC2": {
			"mnemonic": "JP",
			"bytes": 3,
			"cycles": [
				16,
				12
			],
			"operands": [
				{
					"name": "NZ",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC3": {
			"mnemonic": "JP",
			"bytes": 3,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC4": {
			"mnemonic": "CALL",
			"bytes": 3,
			"cycles": [
				24,
				12
			],
			"operands": [
				{
					"name": "NZ",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC5": {
			"mnemonic": "PUSH",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "BC",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC6": {
			"mnemonic": "ADD",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0xC7": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$00",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC8": {
			"mnemonic": "RET",
			"bytes": 1,
			"cycles": [
				20,
				8
			],
			"operands": [
				{
					"name": "Z",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC9": {
			"mnemonic": "RET",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCA": {
			"mnemonic": "JP",
			"bytes": 3,
			"cycles": [
				16,
				12
			],
			"operands": [
				{
					"name": "Z",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCB": {
			"mnemonic": "PREFIX",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCC": {
			"mnemonic": "CALL",
			"bytes": 3,
			"cycles": [
				24,
				12
			],
			"operands": [
				{
					"name": "Z",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCD": {
			"mnemonic": "CALL",
			"bytes": 3,
			"cycles": [
				24
			],
			"operands": [
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCE": {
			"mnemonic": "ADC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0xCF": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$08",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD0": {
			"mnemonic": "RET",
			"bytes": 1,
			"cycles": [
				20,
				8
			],
			"operands": [
				{
					"name": "NC",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD1": {
			"mnemonic": "POP",
			"bytes": 1,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "DE",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD2": {
			"mnemonic": "JP",
			"bytes": 3,
			"cycles": [
				16,
				12
			],
			"operands": [
				{
					"name": "NC",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD3": {
			"mnemonic": "ILLEGAL_D3",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD4": {
			"mnemonic": "CALL",
			"bytes": 3,
			"cycles": [
				24,
				12
			],
			"operands": [
				{
					"name": "NC",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD5": {
			"mnemonic": "PUSH",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "DE",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD6": {
			"mnemonic": "SUB",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xD7": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$10",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD8": {
			"mnemonic": "RET",
			"bytes": 1,
			"cycles": [
				20,
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD9": {
			"mnemonic": "RETI",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDA": {
			"mnemonic": "JP",
			"bytes": 3,
			"cycles": [
				16,
				12
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDB": {
			"mnemonic": "ILLEGAL_DB",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDC": {
			"mnemonic": "CALL",
			"bytes": 3,
			"cycles": [
				24,
				12
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDD": {
			"mnemonic": "ILLEGAL_DD",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDE": {
			"mnemonic": "SBC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xDF": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$18",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE0": {
			"mnemonic": "LDH",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "a8",
					"bytes": 1,
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE1": {
			"mnemonic": "POP",
			"bytes": 1,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE2": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE3": {
			"mnemonic": "ILLEGAL_E3",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE4": {
			"mnemonic": "ILLEGAL_E4",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE5": {
			"mnemonic": "PUSH",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE6": {
			"mnemonic": "AND",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "0"
			}
		},
		"0xE7": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$20",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE8": {
			"mnemonic": "ADD",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "SP",
					"immediate": True
				},
				{
					"name": "e8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "0",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0xE9": {
			"mnemonic": "JP",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEA": {
			"mnemonic": "LD",
			"bytes": 3,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "a16",
					"bytes": 2,
					"immediate": False
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEB": {
			"mnemonic": "ILLEGAL_EB",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEC": {
			"mnemonic": "ILLEGAL_EC",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xED": {
			"mnemonic": "ILLEGAL_ED",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEE": {
			"mnemonic": "XOR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xEF": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$28",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF0": {
			"mnemonic": "LDH",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "a8",
					"bytes": 1,
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF1": {
			"mnemonic": "POP",
			"bytes": 1,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "AF",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "N",
				"H": "H",
				"C": "C"
			}
		},
		"0xF2": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF3": {
			"mnemonic": "DI",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF4": {
			"mnemonic": "ILLEGAL_F4",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF5": {
			"mnemonic": "PUSH",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "AF",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF6": {
			"mnemonic": "OR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0xF7": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$30",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF8": {
			"mnemonic": "LD",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "HL",
					"immediate": True
				},
				{
					"name": "SP",
					"increment": True,
					"immediate": True
				},
				{
					"name": "e8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "0",
				"N": "0",
				"H": "H",
				"C": "C"
			}
		},
		"0xF9": {
			"mnemonic": "LD",
			"bytes": 1,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "SP",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFA": {
			"mnemonic": "LD",
			"bytes": 3,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "a16",
					"bytes": 2,
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFB": {
			"mnemonic": "EI",
			"bytes": 1,
			"cycles": [
				4
			],
			"operands": [],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFC": {
			"mnemonic": "ILLEGAL_FC",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFD": {
			"mnemonic": "ILLEGAL_FD",
			"bytes": 1,
			"cycles": [ 4 ],
			"operands": [ ],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFE": {
			"mnemonic": "CP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				},
				{
					"name": "n8",
					"bytes": 1,
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "1",
				"H": "H",
				"C": "C"
			}
		},
		"0xFF": {
			"mnemonic": "RST",
			"bytes": 1,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "$38",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		}
	},
	"cbprefixed": {
		"0x00": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x01": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x02": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x03": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x04": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x05": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x06": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x07": {
			"mnemonic": "RLC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x08": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x09": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x0A": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x0B": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x0C": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x0D": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x0E": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x0F": {
			"mnemonic": "RRC",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x10": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x11": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x12": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x13": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x14": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x15": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x16": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x17": {
			"mnemonic": "RL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x18": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x19": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x1A": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x1B": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x1C": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x1D": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x1E": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x1F": {
			"mnemonic": "RR",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x20": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x21": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x22": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x23": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x24": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x25": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x26": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x27": {
			"mnemonic": "SLA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x28": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x29": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x2A": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x2B": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x2C": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x2D": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x2E": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x2F": {
			"mnemonic": "SRA",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x30": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x31": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x32": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x33": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x34": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x35": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x36": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x37": {
			"mnemonic": "SWAP",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "0"
			}
		},
		"0x38": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x39": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x3A": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x3B": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x3C": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x3D": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x3E": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x3F": {
			"mnemonic": "SRL",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "0",
				"C": "C"
			}
		},
		"0x40": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x41": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x42": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x43": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x44": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x45": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x46": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x47": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x48": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x49": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x4A": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x4B": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x4C": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x4D": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x4E": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x4F": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x50": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x51": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x52": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x53": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x54": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x55": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x56": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x57": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x58": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x59": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x5A": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x5B": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x5C": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x5D": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x5E": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x5F": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x60": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x61": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x62": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x63": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x64": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x65": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x66": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x67": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x68": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x69": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x6A": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x6B": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x6C": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x6D": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x6E": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x6F": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x70": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x71": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x72": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x73": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x74": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x75": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x76": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x77": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x78": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x79": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x7A": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x7B": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x7C": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x7D": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x7E": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				12
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x7F": {
			"mnemonic": "BIT",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "Z",
				"N": "0",
				"H": "1",
				"C": "-"
			}
		},
		"0x80": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x81": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x82": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x83": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x84": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x85": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x86": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x87": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x88": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x89": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x8A": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x8B": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x8C": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x8D": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x8E": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x8F": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x90": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x91": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x92": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x93": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x94": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x95": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x96": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x97": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x98": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x99": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x9A": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x9B": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x9C": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x9D": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x9E": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0x9F": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA0": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA1": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA2": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA3": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA4": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA5": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA6": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA7": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA8": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xA9": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xAA": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xAB": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xAC": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xAD": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xAE": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xAF": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB0": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB1": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB2": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB3": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB4": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB5": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB6": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB7": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB8": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xB9": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xBA": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xBB": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xBC": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xBD": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xBE": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xBF": {
			"mnemonic": "RES",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC0": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC1": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC2": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC3": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC4": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC5": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC6": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC7": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "0",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC8": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xC9": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCA": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCB": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCC": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCD": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCE": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xCF": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "1",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD0": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD1": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD2": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD3": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD4": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD5": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD6": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD7": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "2",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD8": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xD9": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDA": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDB": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDC": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDD": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDE": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xDF": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "3",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE0": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE1": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE2": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE3": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE4": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE5": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE6": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE7": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "4",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE8": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xE9": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEA": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEB": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEC": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xED": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEE": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xEF": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "5",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF0": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF1": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF2": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF3": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF4": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF5": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF6": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF7": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "6",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF8": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "B",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xF9": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "C",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFA": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "D",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFB": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "E",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFC": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "H",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFD": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "L",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFE": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				16
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "HL",
					"immediate": False
				}
			],
			"immediate": False,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		},
		"0xFF": {
			"mnemonic": "SET",
			"bytes": 2,
			"cycles": [
				8
			],
			"operands": [
				{
					"name": "7",
					"immediate": True
				},
				{
					"name": "A",
					"immediate": True
				}
			],
			"immediate": True,
			"flags": {
				"Z": "-",
				"N": "-",
				"H": "-",
				"C": "-"
			}
		}
	}
}

def opcode(type):
    f.write("struct opcode "+type+"[] = {\n\t")
    hitem = 0
    for key, value in data[type].items():
        #print(value)  # For debugging, check the structure of each opcode

        # Ensure necessary keys exist in the value
        if "bytes" in value and "cycles" in value:
            if hitem == 16:
                f.write("\n\t")
                hitem = 0
            
            f.write("{\"" + value["mnemonic"])
            
            for i in value["operands"]:
                f.write(" " + i["name"])

            f.write("\"," + str(value["bytes"]) + ",")
            f.write(str(value["cycles"][0]))  # Convert cycles to string
            
            if len(value["cycles"]) > 1:
                f.write("/*")
                for cycle in value["cycles"]:
                    f.write(str(cycle) + ",")  # Convert each cycle to string
                f.write("*/")
                
            f.write("}, ")
            hitem += 1
        else:
            print(f"Missing 'bytes' or 'cycles' in item: {value}")
    f.write("\n};")  # Close the struct definition


with open("mogus.txt", "w") as f:
    opcode("unprefixed")
    f.write("\n\n")
    opcode("cbprefixed")