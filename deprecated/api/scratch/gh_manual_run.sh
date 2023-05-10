#!/bin/main

# Closed Issues since Last Release
SEARCHSTR=""
SEARCHSTR="${SEARCHSTR} is:issue"
SEARCHSTR="${SEARCHSTR} closed:>=2022-02-07"
#SEARCHSTR="${SEARCHSTR} no:milestone"
SEARCHSTR="${SEARCHSTR} -label:_deprecated"
SEARCHSTR="${SEARCHSTR} -label:prj.RCE_EOL.Infrastructure"
SEARCHSTR="${SEARCHSTR} -label:prj.RCE_EOL.Migration"
SEARCHSTR="${SEARCHSTR} -label:prj.RCE_EOL.Migration.Deprecated"
SEARCHSTR="${SEARCHSTR} -label:prj.SidNG.Auth"
SEARCHSTR="${SEARCHSTR} -label:prj.HerokuReplacement"
SEARCHSTR="${SEARCHSTR} -label:prj.MetricsDashboard"
	
gh issue list -L 100 -S "${SEARCHSTR}" --json number,title,state,milestone,closedAt,labels --template '{{range .}}{{.number}}{{"|"}}{{.title}}{{"|"}}{{ .state}}{{ "|"}}{{ .milestone.title}}{{ "|"}}{{ .closedAt}}{{ "|" }}{{ range $index, $map :=.labels }} {{$map.name}}{{end}}{{"\n"}}{{end}}'


# map[
# color:9b4dc1 
# description:Sid UX,UI, and Documentation. 
# id:MDU6TGFiZWwyMzU2Mzg2OTI1 
# name:prj.SidNG.UX
# ] 
# 
# map[
# color:7DB175 
# description:This work is a Spike 
# id:LA_kwDODrgDdM7KWhB0 
# name:_spike] 
# map[color:AE2627 description:response to security incident id:LA_kwDODrgDdM7ZElHs name:_securityResponse]]

# WORKS
# gh issue list -L 100 -S "${SEARCHSTR}" --json number,title,state,milestone,closedAt,labels --template '{{range .}}{{tablerow (printf "#%v" .number) "|" .title "|" .state "|" .closedAt "|" .milestone.title "|" .labels[1]["name"] {{end}}'
# gh issue list -L 100 -S "${SEARCHSTR}" --json number,title,state,milestone,closedAt,labels --template '{{range .}}{{tablerow (printf "#%v" .number) "|" .title "|" .state "|" .closedAt "|" .milestone.title "|" }}{{range .labels}}{{ tablerow  .name }}}} {{end }} {{end}}'
# gh issue list -L 100 -S "${SEARCHSTR}" --json number,title,state,milestone,closedAt,labels --template '{{range .}} {{ .title }} {{ "|" }} {{range $index, $map :=.labels }}  {{ $map.name}} {{end}}{{ "\n"}} {{end}}'
# gh issue list -L 100 -S "${SEARCHSTR}" --json number,title,state,milestone,closedAt,labels --template '{{range .}}{{ "|"}} {{ .title}} {{ "|"}} {{ .state}} {{ "|"}} {{ .closedAt}} {{ "|" }} {{ range $index, $map :=.labels }}  {{ $map.name }} {{end}} {{"\n"}} {{end}}'
# gh issue list -L 100 -S "${SEARCHSTR}" --json number,title,state,milestone,closedAt,labels --template '{{range .}}{{ "|"}} {{ .title}} {{ "|"}} {{ .state}} {{ "|"}} {{ .closedAt}} {{ "|" }} {{ $data := "" }} {{ range $index, $map :=.labels }}  {{ $data := $data + $map.name }} {{end}} {{"\n"}} {{end}}'


