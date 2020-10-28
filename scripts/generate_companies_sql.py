companies = """VALE	VALE3	Mineração	9,71%
BRADESCO	BBDC4	Financeiro	8,52%
PETROBRAS	PETR4	Petróleo, Gás e Biocombustíveis	6,95%
B3	B3SA3	Financeiro	4,83%
PETROBRAS	PETR3	Petróleo, Gás e Biocombustíveis	4,76%
AMBEV S/A	ABEV3	Consumo não-cíclico	4,60%
BANCO DO BRASIL	BBAS3	Financeiro	4,05%
ITAUSA	ITSA4	Financeiro	3,43%
JBS	JBSS3	Alimentos processados	2,24%
LOJAS RENNER	LREN3	Comércio	2,15%
ITAU UNIBANCO	ITUB4	Financeiro	10,05%
BRADESCO	BBDC3	Financeiro	1,80%
BRF S/A	BRFS3	Alimentos processados	1,59%
RUMO S/A	RAIL3	Bens industriais	1,46%
SUZANO S/A	SUZB5	Madeira e papel	1,46%
LOCALIZA	RENT3	Locação de veículos	1,41%
TELEF BRASIL	VIVT4	Telecomunicações	1,31%
BB SEGURIDADE	BBSE3	Seguros	1,29%
ULTRAPAR	UGPA3	Petróleo, Gás e Biocombustíveis	1,28%
EQUATORIAL	EQTL3	Energia elétrica	1,09%
KROTON	KROT3	Educacionais	1,08%
SANTANDER BR	SANB11	Financeiro	1,02%
WEG	WEGE3	Bens Industriais	0,99%
CCR S/A	CCRO3	Bens industriais	0,96%
RAIADROGASIL	RADL3	Saúde	0,96%
SABESP	SBSP3	Saneamento	0,95%
MAGAZINE LUIZA	MGLU3	Comércio	0,94%
AZUL	AZUL4	Bens Industriais	0,92%
EMBRAER	EMBR3	Bens industriais	0,83%
GERDAU	GGBR4	Siderurgia e Metalurgia	0,83%
PÃO DE AÇÚCAR - CBD	PCAR4	Consumo não-cíclico	0,83%
CEMIG	CMIG4	Energia elétrica	0,82%
BR MALLS PAR	VRML3	Exploração de imóveis	0,71%
ENGIE BRASIL	ENGIE3	Energia elétrica	0,70%
IRB BRASIL RE	IRBR3	Seguros	0,70%
LOJAS AMERICANAS	LAME4	Comércio	0,69%
HYPERA	HYPE3	Saúde	0,67%
SID NACIONAL	CSNA3	Siderurgia e Metalurgia	0,65%
ELETROBRAS	ELET3	Energia elétrica	0,62%
ESTACIO PART	YDUQ3	Educacionais	0,58%
TIM PART S/A	TIMP3	Telecomunicações	0,58%
KLABIN S/A	KLBN11	Madeira e papel	0,57%
NATURA	NATU3	Consumo não-cíclico	0,57%
BRASKEM	BRKM5	Químicos	0,56%
ELETROBRAS	ELET6	Energia Elétrica	0,53%
PETROBRAS BR	BRDT3	Petróleo, Gás e Biocombustíveis	0,51%
COSAN	CSAN3	Petróleo, Gás e Biocombustíveis	0,45%
CIELO	CIEL3	Financeiro	0,44%
MULTIPLAN	MULT3	Exploração de imóveis	0,44%
BRADESPAR	BRAP4	Mineração	0,43%
CVC BRASIL	CVCB3	Viagens e lazer	0,42%
FLEURY	FLRY3	Saúde	0,42%
TAESA	TAEE11	Energia elétrica	0,36%
B2W DIGITAL	BTOW3	Comércio	0,35%
CYRELA REALT	CYRE3	Construção civil	0,34%
ENERGIAS BR	ENBR3	Energia elétrica	0,33%
MRV	MRVE3	Construção civil	0,33%
QUALICORP	QUAL3	Saúde	0,32%
GOL	GOLL4	Bens industriais	0,30%
USIMINAS	USIM5	Siderurgia e Metalurgia	0,28%
IGUATEMI	IGTA3	Exploração de imóveis	0,24%
GERDAU MET	GOAU4	Siderurgia e Metalurgia	0,23%
VIA VAREJO	VVAR3	Comércio	0,21%
MARFRIG	MRFG3	Alimentos processados	0,15%
ECORODOVIAS	ECOR3	Bens industriais	0,13%
SMILES	SMLS3	Diversos	0,13%"""

companies = companies.split("\n")
companies = [i.split("\t") for i in companies]

template = (
    "INSERT INTO companies (name,symbol,peso,populated) VALUES ('{}','{}','{}',false);"
)
for company in companies:
    peso = company[3][:-2]
    peso = peso.replace(",", ".")
    print(template.format(company[0], company[1], peso))
