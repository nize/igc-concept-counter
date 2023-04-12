# Import libraries
import xml.etree.ElementTree as etree
# Specify XML file name
xml_file = 'business_glossary_xml_sample.xml'
# Parse the XML file
tree = etree.parse(xml_file)
# Define the XML namespace.
namespace = {'bg': 'http://www.ibm.com/is/bg/importexport'}

# Find all synonymGroup elements.
synonym_groups = tree.findall('.//bg:synonymGroup', namespace)

# Count the number of synonymGroup elements.
SG = len(synonym_groups)

# Count the number of term elements.
terms = tree.findall('.//bg:term', namespace)
T = len(terms)

# Count the number of terms in the synonymGroup elements.
synonyms = tree.findall('.//bg:synonymGroup/bg:synonyms/bg:termRef', namespace)
TS = len(synonyms)

# Count the number of terms labelled "type hierarchy dummy"
dummy_terms = [term for term in terms if term.find(".//bg:label[@name='type hierarchy dummy']", namespace) is not None]
DT = len(dummy_terms)

# Calculate the number of concepts
C = SG + T - TS - DT

print(f'There are {SG} synonymGroups. (SG)')
print(f'There are {T} terms. (T)')
print(f'There are {TS} synonyms. (TS)')
print(f'There are {DT} dummy terms. (DT)')
print(f'We are expecting {C} concepts. (C)')

# Count the number of category elements.
categories = tree.findall('.//bg:category', namespace)
Ca = len(categories)

# Count the number of category elements having a name attribute equal to "Individual Concepts"
IC = len([category for category in categories if category.get('name') == 'Individual Concepts'])

# Calculate the number of dictionaries
D = Ca - IC

print(f'There are {Ca} categories. (Ca)')
print(f'There are {IC} categories named "Individual Concepts". (IC)')
print(f'We are expecting {D} dictionaries. (D)')
