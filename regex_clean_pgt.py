#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 06:02:16 2020

@author: snowden
"""

import re

regex = r"Total compte \d\d\d\d\d\d\d\d"

test_str = ("\n"
	"S-DPC| 0566| S01| 1034| 20160101| 20161231		\n"
	"CABINET PAGESTI	Copropriété N° 1034	Page N° 1\n"
	"34 RUE DU FBG SAINT-MARTIN - 75010 PARIS	\n"
	"Détail des DEPENSES de la période du 01/01/2016 au 31/12/2016	\n"
	"Date		Libellés	N° Fact	Montants	Récupérable	Déductible	T.V.A.\n"
	"0001 CHARGES GENERALES					\n"
	"EAU FROIDE						\n"
	"08/02/2016	Facture du 08/02/16 695m3		2303,29	2303,29		166,70\n"
	"Four: EAU & FORCE					\n"
	"09/05/2016	Facture du 09/05/16 688m3		2298,54	2298,54		166,88\n"
	"Four: EAU DE PARIS					\n"
	"08/08/2016	Facture du 08/08/16 669m3		2235,23	2235,23		162,27\n"
	"Four: EAU DE PARIS					\n"
	"07/11/2016	Facture du 07/11/16 660m3		2221,18	2221,18		160,25\n"
	"Four: EAU DE PARIS					\n"
	"Total compte 60100000 EAU FROIDE		9058,24	9058,24		656,10\n"
	"EDF SERVICES GENERAUX					\n"
	"26/01/2016	Facture du 26/01/16		41,67	41,67		5,78\n"
	"Four: E.D.F Entreprises					\n"
	"23/03/2016	Facture du 23/03/16		50,05	50,05		7,18\n"
	"Four: E.D.F Entreprises					\n"
	"23/03/2016	Facture du 23/03/16		84,16	84,16		7,06\n"
	"Four: E.D.F Entreprises					\n"
	"25/05/2016	Facture du 25/05/16		42,59	42,59		5,94\n"
	"Four: E.D.F Entreprises					\n"
	"23/07/2016	Facture du 23/07/16		37,45	37,45		5,08\n"
	"Four: E.D.F Entreprises					\n"
	"24/09/2016	Facture du 24/09/16		35,67	35,67		4,79\n"
	"Four: E.D.F Entreprises					\n"
	"24/09/2016	Facture du 24/09/16		84,07	84,07		6,79\n"
	"Four: E.D.F Entreprises					\n"
	"24/11/2016	Facture du 24/11/16		41,33	41,33		5,72\n"
	"Four: E.D.F Entreprises					\n"
	"Total compte 60200000 EDF SERVICES GENERAUX		416,99	416,99		48,34\n"
	"PRODUITS ENTRETIEN					\n"
	"26/01/2016	Achat ampoules 2015		425,64	425,64		70,94\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"11/03/2016	Fourniture trimestrielle		106,29	106,29		17,72\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"10/06/2016	Fourniture trimestrielle		106,29	106,29		17,72\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"12/09/2016	Fourniture trimestrielle		106,29	106,29		17,72\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"10/12/2016	Fourniture trimestrielle		106,80	106,80		17,80\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"Total compte 60410000 PRODUITS ENTRETIEN		851,31	851,31		141,90\n"
	"ENTRETIEN IMMEUBLE					\n"
	"11/01/2016	Entretien 01/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"11/02/2016	Entretien 02/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"11/03/2016	Entretien 03/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"11/04/2016	Entretien 04/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"11/05/2016	Entretien 05/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"10/06/2016	Entretien 06/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"10/07/2016	Entretien 07/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"10/08/2016	Entretien 08/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"12/09/2016	Entretien 09/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"12/10/2016	Entretien 10/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"10/11/2016	Entretien 11/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"10/12/2016	Entretien 12/16			605,45	605,45		100,91\n"
	"Four:S.A.R.L. T.P.V.S.					\n"
	"Total compte 61100000 ENTRETIEN IMMEUBLE		7265,40	7265,40		1210,92\n"
	"CONTRAT EXTINCTEURS					\n"
	"22/03/2016	Vérification extincteur		55,67		55,67	9,28\n"
	"Four:Société SICLI					\n"
	"Total compte 61400001 CONTRAT EXTINCTEURS		55,67		55,67	9,28\n"
	"DEPENSES DIVERSES N/REC.					\n"
	"12/01/2016	fourniture clef porte entrée Mme CAVALLI		15,40CR			2,54CR\n"
	"19/08/2016	Founiture 1clef à Mme NADIRAS		10,00CR			1,66CR\n"
	"29/09/2016	Fourniture 2 Clefs porte à SCI GENIDAN		25,32CR			0,01CR\n"
	"Total compte 61500001 DEPENSES DIVERSES N/REC.		50,72CR			4,21CR\n"
	"PETITS TRVX DE PLOMBERIE					\n"
	"01/04/2016	Fuite sur vanne d'arrêt		170,50	170,50		15,50\n"
	"Edité le 12/06/2017 à 09:34")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.