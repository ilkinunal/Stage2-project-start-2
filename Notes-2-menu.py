list_menu1 =["Web &#38; HTML  for Beginners", "Definitions", "How the Web Works?", "HTML"] 
list_menu2 =["HTML &#38; CSS &#38; DOM","WebPage ingredients", "Text Editors for coding", "Avoiding Repetition"] 
list_menu3 =["Python", "Introduction to Programming", "Variables &#38; Strings &#38; Lists", "Input&#8594;Function&#8594;Output",
             "Control Flow &#38; Loops &#38; Operators"]

def generate_menu(list_menu1,list_menu2,list_menu3):
    def generate_menu1(list_menu1):
        txt1= '''
  <div>
  <h2>menu </h2>
    <ul>
    <li class="sub-menu"><a href="#link1">'''+list_menu1[0]+'''
      <ul class="menu">
        <li class="sub-menu"><a href="#link1.1">'''+ list_menu1[1]+'''
        <li class="sub-menu"><a href="#link1.2">'''+ list_menu1[2]+'''
        <li class="sub-menu"><a href="#link1.3">'''+ list_menu1[3]+'''
      </ul> 
    </li>'''
        return txt1
    def generate_menu2(list_menu2):
        txt2= '''
    <li class="sub-menu"><a href="#link2">'''+list_menu2[0]+'''
      <ul class="menu">
        <li class="sub-menu"><a href="#link2.1">'''+ list_menu2[1]+'''
        <li class="sub-menu"><a href="#link2.2">'''+ list_menu2[2]+'''
        <li class="sub-menu"><a href="#link2.3">'''+ list_menu2[3]+'''
      </ul> 
    </li>'''
        return txt2
    def generate_menu3(list_menu3):
        txt3= '''
    <li class="sub-menu"><a href="#link3">'''+list_menu3[0]+'''
      <ul class="menu">
        <li class="sub-menu"><a href="#link3.1">'''+ list_menu3[1]+'''
        <li class="sub-menu"><a href="#link3.2">'''+ list_menu3[2]+'''
        <li class="sub-menu"><a href="#link3.3">'''+ list_menu3[3]+'''
        <li class="sub-menu"><a href="#link3.4">'''+ list_menu3[4]+'''
      </ul> 
    </li>
    </ul>
</div>  '''
        return txt3
    return generate_menu1(list_menu1) + generate_menu2(list_menu2) + generate_menu3(list_menu3)

print generate_menu(list_menu1,list_menu2,list_menu3)
