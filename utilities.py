#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Genre Classifier
#
# Copyright (C) 2016 Juliette Lonij, Koninklijke Bibliotheek -
# National Library of the Netherlands
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

genres = {
    1: ['Nieuwsbericht'],
    2: ['Interview'],
    3: ['Reportage/feature'],
    4: ['Verslag'],
    5: ['Opiniestuk', 'Hoofdredactioneel commentaar'],
    6: ['Recensie'],
    7: ['Achtergrond/Nieuwsanalyse'],
    8: ['Column']
}

features = [
    'direct_quotes',
    'remaining_quote_chars',
    #'tokens',
    'sentences',
    'avg_sentence_length',
    #'digits',
    'digits_perc',
    'currency_symbols',
    'currency_symbols_perc',
    'exclamation_marks',
    'exclamation_marks_perc',
    'question_marks',
    'question_marks_perc',
    'pronoun_1',
    'pronoun_1_perc',
    'pronoun_1_perc_rel',
    'pronoun_2',
    'pronoun_2_perc',
    'pronoun_2_perc_rel',
    'pronoun_3',
    'pronoun_3_perc',
    'pronoun_3_perc_rel',
    'adjectives',
    'adjectives_perc',
    'modal_verbs',
    'modal_verbs_perc',
    'modal_adverbs',
    'modal_adverbs_perc',
    'intensifiers',
    'intensifiers_perc',
    'cogn_verbs',
    'cogn_verbs_perc',
    'named_entities',
    'named_entities_perc',
    'named_entities_pos',
    'unique_named_entities',
    'self_cl_1',
    'self_cl_2',
    'self_cl_3',
    'self_cl_4',
    'self_cl_5',
    'self_cl_6',
    'self_cl_7',
    'self_cl_8',
    'self_cl_3-4',
    'self_cl_3-8'
]

pronouns_1 = [
    'ik',
    'mij',
    'me',
    'mijn',
    'wij',
    'we',
    'ons'
]

pronouns_2 = [
    'jij',
    'je',
    'jou',
    'jouw',
    'jullie',
    'u',
    'uw'
]

pronouns_3 = [
    'hij',
    'hem',
    'zij',
    'ze',
    'zijn',
    'haar',
    'hun',
    'hen',
    'zich'
]

modal_verbs = [
    'Behoeven',
    'Blijken',
    'Dunken',
    'Heten',
    'Hoeven',
    'Lijken',
    'Kunnen',
    'Moeten',
    'Mogen',
    'Schijnen',
    'Toeschijnen',
    'Voorkomen',
    'Willen',
    'Zullen'
]

modal_adverbs = [
    'Allicht',
    'Blijkbaar',
    'Eigenlijk',
    'Gelukkig',
    'Godweet',
    'Helaas',
    'Hoofdzakelijk',
    'Hoogstwaarschijnlijk',
    'Hopelijk',
    'Jammer',
    'Kennelijk',
    'Misschien',
    'Mogelijk',
    'Natuurlijk',
    'Ongelukkigerwijs',
    'Ongetwijfeld',
    'Onmogelijk',
    'Onwaarschijnlijk',
    'Schijnbaar',
    'Stellig',
    'Tevergeefs',
    'Trouwens',
    'Tuurlijk',
    'Uiteraard',
    'Vergeefs',
    'Vermoedelijk',
    'Waarlijk',
    'Waarschijnlijk',
    'Wellicht',
    'Wieweet',
    'Zeker',
    'Zogenaamd',
    'Zonder twijfel'
]

intensifiers = [
    'Aanmerkelijk',
    'Aanzienlijk',
    'Bijna',
    'Behoorlijk',
    'Drastisch',
    'Echt',
    'Enigszins',
    'Enorm',
    'Erg',
    'Extra',
    'Flink',
    'Gewoon',
    'Godsgruwelijk',
    'Hartstikke',
    'Helemaal',
    'Hoezeer',
    'Nagenoeg',
    'Nauwelijks',
    'Nogal',
    'Oneindig',
    'Ongemeen',
    'Ongeveer',
    'Ontzettend',
    'Onuitsprekelijk',
    'Onwijs',
    'Pakweg',
    'Uitdrukkelijk',
    'Uitermate',
    'Uitsluitend',
    'Voldoende',
    'Volkomen',
    'Volledig',
    'Vooral',
    'Voornamelijk',
    'Vreselijk',
    'Vrijwel',
    'Welhaast',
    'Zo',
    'Zoveel',
    'Zowat'
]

cogn_verbs = [
    'Aankondigen',
    'Aarzelen',
    'Aannemen',
    'Achten',
    'Afwijzen',
    'Afleiden',
    'Bedenken',
    'Bedoelen',
    'Begrijpen',
    'Bekennen',
    'Beloven',
    'Beslissen',
    'Betreuren',
    'Betwijfelen',
    'Concluderen',
    'Denken',
    'Dreigen',
    'Geloven',
    'Herinneren',
    'Herkennen',
    'Hopen',
    'Menen',
    'Opmerken',
    'Prefereren',
    'Reageren',
    'Realiseren',
    'Suggereren',
    'Uitleggen',
    'Uitsluiten',
    'Uitvinden',
    'Vaststellen',
    'Verdenken',
    'Vergeten',
    'Verlangen',
    'Vermoeden',
    'Vernemen',
    'Veronderstellen',
    'Vertrouwen',
    'Verwachten',
    'Vinden',
    'Voelen',
    'Voorstellen',
    'Vragen',
    'Vrezen',
    'Waarschuwen',
    'Wensen',
    'Weten'
]

self_classifications = {
    '1': ['nieuwsbericht', 'nieuwsartikel'],
    '2': ['interview', 'tweegesprek', 'vraaggesprek', 'interviewen'],
    '3': ['reportage', 'sfeerverslag', 'ooggetuigeverslag',
            'reconstructie', 'reisverslag'],
    '4': [],
    '5': ['opiniestuk', 'commentaar', 'opinie', 'betoog',
            'hoofdartikel', 'betogen'],
    '6': ['recensie', 'boekbespreking', 'filmkritiek', 'theaterkritiek',
            'filmbespreking', 'theaterbespreking'],
    '7': ['nieuwsanalyse', 'analyse', 'achtergrond',
            'achtergrondartikel', 'beschouwing'],
    '8': ['column', 'cursiefje', 'rubriek'],
    '3-4': ['verslag'],
    '3-8': ['kroniek']
}
