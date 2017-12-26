#!/bin/sh

if (( $# != 2 )); then
    echo "invalid number of parameters (text input file, wav output file)"
    exit 1
fi

build/bin/flite_hts_engine \
     -td build/hts_voice_cstr_uk_female-1.0/tree-dur.inf -tf build/hts_voice_cstr_uk_female-1.0/tree-lf0.inf -tm build/hts_voice_cstr_uk_female-1.0/tree-mgc.inf \
     -md build/hts_voice_cstr_uk_female-1.0/dur.pdf         -mf build/hts_voice_cstr_uk_female-1.0/lf0.pdf       -mm build/hts_voice_cstr_uk_female-1.0/mgc.pdf \
     -df build/hts_voice_cstr_uk_female-1.0/lf0.win1        -df build/hts_voice_cstr_uk_female-1.0/lf0.win2      -df build/hts_voice_cstr_uk_female-1.0/lf0.win3 \
     -dm build/hts_voice_cstr_uk_female-1.0/mgc.win1        -dm build/hts_voice_cstr_uk_female-1.0/mgc.win2      -dm build/hts_voice_cstr_uk_female-1.0/mgc.win3 \
     -cf build/hts_voice_cstr_uk_female-1.0/gv-lf0.pdf      -cm build/hts_voice_cstr_uk_female-1.0/gv-mgc.pdf    -ef build/hts_voice_cstr_uk_female-1.0/tree-gv-lf0.inf \
     -em build/hts_voice_cstr_uk_female-1.0/tree-gv-mgc.inf -k  build/hts_voice_cstr_uk_female-1.0/gv-switch.inf -o "$2" \
     -s  48000.0\
     -p  240.0\
     -a  0.55\
     -g  0.0\
     -b  0.2\
     -u  0.5\
     -jm 0.8 \
     "$1"
