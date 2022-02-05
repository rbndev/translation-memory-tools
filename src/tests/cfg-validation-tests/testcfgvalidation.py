#
# Copyright (c) 2021 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from builder.jsonbackend import JsonBackend
from builder.projects import Projects
import unittest
from os import path
import json
from builder.licenses import Licenses


class TestCfgValidation(unittest.TestCase):

    def get_projects_cfg(self):
        projects_dir = path.dirname(path.realpath(__file__))
        projects_dir += '/../../../cfg/projects/'
        json = JsonBackend(projects_dir, validation = True)
        json.load()
        return json

    def test_cfg_validation(self):
        json = self.get_projects_cfg()

        self.assertGreater(len(json.projects), 1)

        # Check filesets
        projects = Projects()
        for project_dto in json.projects:
            projects.add_project(project_dto, add_source = True)

    def test_check_license(self):
        json = self.get_projects_cfg()

        valid_licenses_ids = Licenses().get_licenses_ids()
        for project in json.projects:
            license_id = project.license
            if len(license_id) == 0:
                continue

            self.assertIn(license_id, valid_licenses_ids)

if __name__ == '__main__':
    unittest.main()
