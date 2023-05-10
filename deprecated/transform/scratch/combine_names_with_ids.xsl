<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl">
<xsl:output method="xml" indent="yes" encoding="utf-8" omit-xml-declaration="yes"/>
<!--<xsl:variable name="secondXmlDoc" select="document('~/DevCode/import_xml_to_vp/0/wrk/combined_id_name_list.xml')"/>-->

    <xsl:template match="@* | node()">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>
 
    <!--
        locate the element that contains this ID
        Then change the name attribute
    -->
   
    <xsl:template match="ImageShape[@Id = 'sf_Wq36GAqBCARX.'][@Name]" >
        <xsl:copy>
            <xsl:attribute name='Name' >Create glossary</xsl:attribute>
            <xsl:apply-templates select="@*[name(.)!='Name']" />
            <xsl:apply-templates select="node()"/>
        </xsl:copy>
    </xsl:template>
    
    
</xsl:stylesheet>