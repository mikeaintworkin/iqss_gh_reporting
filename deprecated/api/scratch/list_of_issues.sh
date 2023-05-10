#!/bin/main
# export GITHUB_TOKEN=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
# export GH_REPO=hmdc/DevOpsProjects

while read -r line;
do
   #echo "$line" ;
   NUMB=$(echo $line | cut -d' ' -f1)
   #gh issue view ${NUMB} --json number,title,state,milestone,closedAt --template '{{printf "#%v" .number}} {{.title}} {{.state}} {{.closedAt}} {{printf "\n"}}'
   #gh issue view ${NUMB} --json number,title,state,milestone,closedAt --template '{{printf "#%v" .number}} {{.title}} {{.state}} {{printf "\n"}}'
   gh issue view ${NUMB} --json number,title,state,milestone,closedAt,labels --template '{{.number}}|{{.title}}{{ "|"}}{{ .state}}{{ "|"}}{{ .closedAt}}{{ "|" }}{{ range $index, $map :=.labels }} {{$map.name}}{{end}}{{"\n"}}'
done < ../input/input.txt