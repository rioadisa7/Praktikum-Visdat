import streamlit as st

#  text element
#  header untuk membuat tulisan header
# st.header ("ini header")
# st.subheader("ini sub header")
# st.text("ini teks biasa tanpa format")
# st.markdown("**ini teks  bold** dan *ini teks italic*")
# st.caption("ini caption")
# st.title("ini judul")

# st.title("Praktikum 1")
#     st.subheader("Text Element")
#     st.markdown("""
#     1. Rio Adi Saputro
#     2. 0110122076
#     """)

#bagian 2: Menampilkan Rumus (Latex)
st.header("Displaying LaTex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''')
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab''')

st.header ("Displaying Code")
st.subheader("Python Code")

code = '''
def hello():
    print("Hello, Streamlit)
'''

st.code(code, language='python')

st.subheader("Java Code")
st.code('''
    public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello  World:);
        }
    }
''', language='java')

st.subheader("Javascript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    adddlert("Welcome guest!);
}
catch(err) {
    document.getElementById("demo").innerHTML = err.massage; 
}
</script>

""", language='javascript')