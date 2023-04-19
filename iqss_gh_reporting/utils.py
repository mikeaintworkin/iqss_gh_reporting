# Credits: ChatGPT
import datetime
import json

# Use PyGithub to get the project cards
from github import Github
from typing import Literal
import re
from pathvalidate import sanitize_filename


class GithubProjectCards:
    def __init__(self, access_token: str, organization_name: str, project_name: str, out_dir: str):
        #external init
        self.client = Github(access_token, per_page=100)
        self.organization = self.client.get_organization(organization_name)
        self.project_name = project_name
        self.out_dir = out_dir

        #internal init
        self.card_count = 0
        self.project_cards = []
        self.date_stamp = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        # prereq: out_dir and outputfile are assumed to be valid
        self.out_dir = out_dir
        self.outputfile =  self.date_stamp + "-" + sanitize_filename(project_name)  + "-legacy"


    def get_project_cards(self):
        projects = self.organization.get_projects()
        project = None
        self.card_count = 0

        for p in projects:
            print(f"projects: looking to match {self.project_name} with {p.name}")
            if p.name == self.project_name:
                project = p
                break

        if project is not None:
            columns = project.get_columns()
            for column in columns:
                column_name = column.name
                cards = column.get_cards()
                print(f"start: {self.card_count} cards processed: {project.name}, Column {column.name}")
                for card in cards:
                    self.card_count += 1
                    card_content = card.get_content()
                    #
                    if card_content is not None:
                        regex1 = re.compile(r"(/issues/|/pull/)")
                        regex2 = re.compile(r"(issues|pull)")
                        card_type = regex1.search(card_content.html_url).group(0)
                        card_type = regex2.search(card_type).group(0)
                        if self.card_count % 50 == 0:
                            print(f">>>>>> {self.card_count} cards processed: {project.name}: Column {column.name} ,{card_type} ,{card_content.number} ,{card_content.repository.name} ,{card_content.title}")


                        # do I care about the actual type returned?
                        # if card_content.type in [Literal"Issue", Literal"PullRequest"]:

                        self.project_cards.append({
                            "project": project.name,
                            "column": column_name,
                            "card": card_content.title,
                            "card_url": card_content.html_url,
                            "card_type": card_type,
                            "number": card_content.number,
                            "labels": card_content.labels,
                            "repo": card_content.repository.name,
                            "state": card_content.state,
                            "created_at": card_content.created_at,
                            "updated_at": card_content.updated_at,
                            "closed_at": card_content.closed_at

                        })
                print(f"  end: {self.card_count} cards processed: {project.name}, Column {column.name}")
        return

    def print_project_cards(self):
        header = ["Project", "Column", "Card", "Card URL", "Card Type", "Number", "Repo"]
        print("\t".join(header))

        for card in self.project_cards:
            row = [card['project'], card['column'], card['card'], card['card_url'], card['card_type'], str(card['number']), card['repo']]
            lineout = "'" + "'\t'".join(row) + "'\n"
            print(lineout)

    def save_project_cards(self):
        print(f"Saving result to file.")
        print(f" {self.outputfile}.csv")
        with open(self.outputfile + ".csv", "w") as output_file:
            header = ["Project", "Column", "Card", "Card URL", "Card Type", "Number", "Repo"]
            headerline = "\t".join(header) + "\n"
            output_file.write(headerline)
            for card in self.project_cards:
                row = [card['project'], card['column'], card['card'], card['card_url'], card['card_type'], str(card['number']), card['repo']]
                lineout = "'" + "'\t'".join(row) + "'\n"
                output_file.write(lineout)


