<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl">
<xsl:output method="xml" indent="yes" encoding="utf-8" omit-xml-declaration="yes"/>
<!--<xsl:variable name="secondXmlDoc" select="document('~/DevCode/import_xml_to_vp/0/wrk/')"/>-->
    <xsl:param name="fileName" select="'../../wrk/combined_id_name_list.xml'" />
    <xsl:param name="updates" select="document($fileName)" />
    <xsl:variable name="updateItems" select="$updates/list" />

    <xsl:template match="node() | @*">
        <xsl:copy>
            <xsl:apply-templates select="node() | @*"/>
        </xsl:copy>
    </xsl:template>
 
    <xsl:template match="ModelChildren/Package/ModelChildren/*" >
        
        <xsl:call-template name="LoopIt" >
            <xsl:with-param name="thisImageShapeId" select="./@Id" /> 
        </xsl:call-template>
        <xsl:apply-templates select="node()"/>
        
    </xsl:template>
    



    <!--
        locate the element that contains this ID
        Then change the name attribute
    -->




    <!-- So far I found the image shapes in XML0
    -->
    <xsl:template name="LoopIt" > 
        <xsl:param name="thisImageShapeId" />
        <!--
        <xsl:value-of select="$thisImageShapeId" />
        <xsl:value-of select="$updateItems/item[@Id=$thisImageShapeId]/name" />
        -->
           <xsl:copy>
               <xsl:apply-templates select="@*[name(.)!='Name']" />
               <xsl:attribute name='Name' ><xsl:value-of select="$updateItems/item[@Id=$thisImageShapeId]/name" /></xsl:attribute>
           </xsl:copy>

                
    </xsl:template>
    
    
</xsl:stylesheet>