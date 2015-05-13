list_linkid =["1.1","1.2","1.3","2.1","2.2","2.3","3.1","3.2","3.3","3.4"]
list_title=["Web &#38; HTML  for Beginners","HTML &#38; CSS &#38; DOM","Python"]
list_subtitle =["Definitions","How the Web Works?","HTML"]

def generate_page(list_title,list_linkid):
    def generate_section(list_title):
        m=0
        for m in len(list_title):
            sec= '''
  <div id="link'''+m+'''">
  <h2>''' list_title[m] '''</h2>'''
        def generate_subsection(list_linkid):
            n=0
            for n in len(list_linkid):
                if list_linkid[n][0]==m+1
                sub= '''
    <div>
      <div id="link'''+list_linkid[n]+'''" class="subtitle">''' + list_subtitle[n] +''' </div>
    </div> '''
                return sub
  '''</div>'''
            return sec

    return def generate_section(list_title)

print generate_page(list_title,list_linkid)

      
    
    

