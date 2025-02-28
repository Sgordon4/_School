-------------------------------------------------------------------------
-- Sean Gordon
-- CprE 281
-- Section C/10:00 a.m. Friday
-------------------------------------------------------------------------

-- Mips Processor, Center
-------------------------------------------------------------------------
-- DESCRIPTION: This file contains the center portion of the MIPS 
-- processor, beginning at the input of machine code instruction and 
-- WriteData, and ending at the output of the ALU, ReadData2, and the
-- Sign Extension for the PC register.
--
--
-- NOTES:
-- 2/25/19 by SG::Design created.
-------------------------------------------------------------------------


library IEEE;
use IEEE.std_logic_1164.all;

entity Center is
   generic(N : integer := 32);
   port(clk			: in std_logic;
		iRst		: in std_logic;							-- Used to reset regs
		instr		: in std_logic_vector(31 downto 0);		-- Incoming MIPS machine code
		WriteData	: in std_logic_vector(31 downto 0);		-- Incoming data to write to reg file
		
		----- Control Signals -----
		RegDst		: in std_logic;
		RegWr		: in std_logic;
		ALUSrc		: in std_logic;
		--ALUOp		: in std_logic_vector(1 downto 0);		-- No longer exists, now implemented in control unit
		ALUCtrl		: in std_logic_vector(3 downto 0);		-- What ALUControl would have output, control does now
		
		----- Output Signals -----
		--Read1Out	: out std_logic_vector(31 downto 0);
		Read2Out	: out std_logic_vector(31 downto 0);
		ALUOut		: out std_logic_vector(31 downto 0);
		ALUZero		: out std_logic;
		SExtOut		: out std_logic_vector(31 downto 0));
		
end Center;

architecture structure of Center is
	
	component Mux2to1
	   port(i_A  : in std_logic_vector;
			i_B  : in std_logic_vector;
			i_S  : in std_logic;
			o_F  : out std_logic_vector);
	end component;
	
	component RegFile
	   port(iCLK		: in std_logic;
			iRst		: in std_logic;			-- Reset all regs
			RegWrite	: in std_logic;			-- Reg File enable
			
			ReadAddr1	: in std_logic_vector;	-- Mux1 select
			ReadAddr2	: in std_logic_vector;	-- Mux2 select
			WriteAddr	: in std_logic_vector;
			
			WriteData	: in std_logic_vector;	-- Data to be written
		
			ReadData1	: out std_logic_vector;	-- Mux1 output
			ReadData2	: out std_logic_vector);
	end component;
	
	component SignExtend
	   port(A			: in std_logic_vector;
			S			: in std_logic;
			F			: out std_logic_vector);
	end component;
	
	-- No longer exists, now implemented in control unit
	-- component ALUControl
	   -- port(Instr		: in std_logic_vector;		-- Bits [5-0] of machine instruction
			-- ALUOp		: in std_logic_vector;		-- ALUOp signal from control module
			-- ALUControl	: out std_logic_vector);
	-- end component;
	
	component ALU
	   port(i_A			: in std_logic_vector;
			i_B			: in std_logic_vector;
			i_Samt		: in std_logic_vector;
			ALUCtrl		: in std_logic_vector;
			
			ovf			: out std_logic;
			zero		: out std_logic;
			Cout		: out std_logic;
			o_F			: out std_logic_vector);
	end component;

	
	
	signal s_mux_writeAddr	: std_logic_vector(4 downto 0);		-- Mux before WriteAddr (Uses RegDst)
	signal s_signExtended	: std_logic_vector(31 downto 0);	-- Result of sign extend
	signal s_ReadData1		: std_logic_vector(31 downto 0);	-- Output of RegFile ReadData1
	signal s_ReadData2		: std_logic_vector(31 downto 0);	-- Output of RegFile ReadData2
	signal s_ALU_B			: std_logic_vector(31 downto 0);	-- Mux before ALU (input B, uses ALUSrc)
	--signal s_ALUOp		: std_logic_vector(3 downto 0);		-- Result of ALUControl, now unused, done inside control unit
	--signal s_ALU_out		: std_logic_vector(31 downto 0);	-- Result of ALU
	signal s_ALU_ovf		: std_logic;						-- Result of ALU overflow, just putting it in limbo
	signal s_ALU_Cout		: std_logic;						-- Result of ALU Cout, just putting it in limbo
	
begin

	mux1: Mux2to1
	   port map(i_A		=> Instr(20 downto 16),
				i_B		=> Instr(15 downto 11),
				i_S		=> RegDst,
				o_F		=> s_mux_writeAddr);
				
	regs: RegFile
	   port map(iCLK		=> clk,
				iRst		=> iRst,
				RegWrite	=> RegWr,
				
				ReadAddr1	=> Instr(25 downto 21),
				ReadAddr2	=> Instr(20 downto 16),
				WriteAddr	=> s_mux_writeAddr,
				
				WriteData	=> WriteData,
				
				ReadData1	=> s_ReadData1,
				ReadData2	=> s_ReadData2);
				
	SEXT: SignExtend
	   port map(A		=> Instr(15 downto 0),
				S		=> '1',		-- I actually don't know where this signal should come from
				F		=> s_signExtended);
	
	mux2: Mux2to1
	   port map(i_A		=> s_ReadData2,
				i_B		=> s_signExtended,
				i_S		=> ALUSrc,
				o_F		=> s_ALU_B);
	
	-- No longer exists, now implemented in control unit
	-- ALUCtrl: ALUControl
	   -- port map(Instr		=> Instr(5 downto 0),
				-- ALUOp		=> ALUOp,
				-- ALUControl	=> s_ALUOp);
	
	aluBody: ALU
	   port map(i_A		=> s_ReadData1,
				i_B		=> s_ALU_B,
				i_Samt	=> Instr(10 downto 6),
				ALUCtrl => ALUCtrl,				-- Input directly from control unit
				
				ovf		=> s_ALU_ovf,
				zero	=> ALUZero,
				Cout	=> s_ALU_Cout,
				o_F		=> ALUOut);
	
	
	--Read1Out<= s_ReadData1;
	Read2Out<= s_ReadData2;
	SExtOut	<= s_signExtended;
	
end structure;
	
	
	
	
	
	
	
	
	
	
	
	