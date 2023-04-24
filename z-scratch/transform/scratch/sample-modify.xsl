<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
        <xsl:output method="xml" indent="no" encoding="UTF-8" />
        
        <xsl:template match="node()|@*">
            <xsl:copy>
                <xsl:apply-templates select="node()|@*"/>
            </xsl:copy>
        </xsl:template>
        
        <xsl:template match="/body/foo[@a1='wrong'][@a2]" >
            <xsl:copy>
                <xsl:attribute name="a1">right</xsl:attribute>
                <xsl:apply-templates select="@*[name(.)!='a1' and name(.)!='a2']" />
                <xsl:apply-templates select="node()"/>
            </xsl:copy>
        </xsl:template>
        
</xsl:stylesheet>