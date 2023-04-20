# Credits: ChatGPT
import datetime
import json

# Use PyGithub to get the project cards
from github import Github
from typing import Literal
import re
from pathvalidate import sanitize_filename
import pandas as pd




class GithubProjectCardsPandas:
    def __init__(self, access_token: str, organization_name: str, project_name: str, out_dir: str):
        # external init
        self.client = Github(access_token, per_page=100)
        self.organization = self.client.get_organization(organization_name)
        self.project_name = project_name
        self.out_dir = out_dir

        # internal init
        self.card_count = 0
        self.project_cards = pd.DataFrame(columns=["Project", "Column", "Card", "CardURL", "CardType", "Number", "Labels", "Repo", "State", "CreatedAt", "UpdatedAt", "ClosedAt"])
        self.date_stamp = pd.Timestamp.now().strftime("%Y_%m_%d-%H_%M_%S")
        # prereq: out_dir and outputfile are assumed to be valid
        self.out_dir = out_dir
        self.outputfile = self.date_stamp + "-" + sanitize_filename(project_name)  + "-legacy"

    def get_project_cards(self):
        projects = self.organization.get_projects()
        project = None
        self.card_count = 0

        # find our project
        for p in projects:
            print(f"projects: looking to match {self.project_name} with {p.name}")
            if p.name == self.project_name:
                project = p
                break
        # Let's get the cards
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

                        new_row = {
                            "Project": project.name,
                            "Column": column_name,
                            "Card": card_content.title,
                            "CardURL": card_content.html_url,
                            "CardType": card_type,
                            "Number": card_content.number,
                            "Labels": card_content.labels,
                            "Repo": card_content.repository.name,
                            "State": card_content.state,
                            "CreatedAt": card_content.created_at,
                            "UpdatedAt": card_content.updated_at,
                            "ClosedAt": card_content.closed_at
                        }
                        self.project_cards = pd.concat([self.project_cards, pd.DataFrame([new_row])], ignore_index=True)


                print(f"  end: {self.card_count} cards processed: {project.name}, Column {column.name}")
        return

    def print_project_cards(self):
        print(self.project_cards.to_string(index=False))

    def save_project_cards(self):
        output_to = self.out_dir + "/" + self.outputfile + ".tsv"
        print(f"Saving result to file.")
        print(f" {output_to}")
        self.project_cards.to_csv(output_to, sep='\t', index=False)

    # def save_project_cards_to_xml(self):
    #     output_to = self.out_dir + "/" + self.outputfile + ".xml"
    #     print(f"Saving result to file.")
    #     print(f" {output_to}")
    #     self.project_cards.to_xml(output_to, root_name="project_cards", row_name="card", index=False)

