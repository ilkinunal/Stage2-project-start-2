list_linkid =[1.1,1.2,1.3,2.1,2.2,2.3,3.1,3.2,3.3,3.4]
list_title=["Web &#38; HTML  for Beginners","HTML &#38; CSS &#38; DOM","Python"]
list_subtitle1 =["Definitions","How the Web Works?","HTML"]

def generate_section(list_title):
    m=0
    for m in len(list_title):
        sec= '''
  <div id="link'''+m+'''">
  <h2>''' list_title[m] '''</h2>
  </div>'''
    return sec

print generate_section(list_title)
