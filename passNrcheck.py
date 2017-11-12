#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#purpose: calculate check digits for machine readable passports
# see also: https://pinetik.blogspot.co.at/2011/03/prufziffer-fur-neuen-reisepass.html
# https://www.icao.int/Security/mrtd/Downloads/Doc%209303/Doc%209303%20English/Doc%209303%20Part%201%20Vol%201.pdf#search=Doc%209303%20Part%201%20Vol%201
#
# passnum format: 
#sernum	checkdigit(sernum)	 	NationIdentifier	birthdate (inverse/yymmdd) checkdigit(birthdate)	gender(m/f)	expirationdate (invers/yymmdd)	checkdigit(expirationdate) <<...<< checkdigit(overall)

from itertools import cycle
import argparse

def calc_checknum(strnumpart, weight, debug=False):
    pruefadd = 0
    addseq = []
    for snc,g in zip(strnumpart,cycle(weight)):
        if snc.isalpha():
            o = ord(snc)-55
            si = o
        else:
            si = int(snc)
        gi = int(g)
        prod = si*gi
        pruefadd += prod % 10
        addseq.append(si)
        if debug:
            print(si, gi, si*gi, str(prod)[-1],  pruefadd, sep = "\t")
    serpruef = pruefadd % 10
    addseq.append(serpruef)
    return (serpruef,addseq)

ap = argparse.ArgumentParser(description="calculate check digits for passport numbers")
ap.add_argument("-s", "--sernum", required=True, dest="sernum", help="Passport serial e.g. P1239999")
ap.add_argument("-b", "--birthdate", required=True, dest="birthdate", help="Birthdate in yymmtt format e.g. 001224 ")
ap.add_argument("-e", "--expirationdate", required=True, dest="expirationdate", help="Expiration date in yymmtt format")
ap.add_argument("-w", "--weightsequence", required=False, dest="weight", help="weightsequence to use", default="731")

if __name__ == "__main__":
    args = ap.parse_args()
    
    scheck, serparts = calc_checknum(args.sernum, args.weight)
    bdcheck, bdparts = calc_checknum(args.birthdate, args.weight)
    edcheck, adparts = calc_checknum(args.expirationdate, args.weight)
    addprod = 0
    #print(serparts+bdparts+adparts)
    #calc overall checksum
    for n,g in zip(serparts+bdparts+adparts, cycle(args.weight)):
        prod = n*int(g)
        add = prod % 10
        addprod += add
        #print(n, g, prod, add, sep="\t")

    fullcheck = addprod % 10
    print("sernum\t", "check", "birthd", "check", "expire", "check", "overall check", sep="\t")
    print(args.sernum, scheck, args.birthdate, bdcheck, args.expirationdate, edcheck, fullcheck, sep="\t")
