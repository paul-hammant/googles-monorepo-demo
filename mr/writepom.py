import sys
import os.path
for pom_template in sys.stdin:
    pom_template = pom_template.strip()
    dirname = os.path.dirname(pom_template)
    with open(pom_template) as f:
        if os.path.exists(dirname + '/pom.xml'):
            os.chmod(dirname + '/pom.xml', 0755)
        with open(dirname + '/pom.xml', 'w') as the_pom:
            lines = f.readlines()
            for line in lines:
                if line.strip().startswith("<module>") and line.strip().endswith("</module>"):
                    sub_project = line.strip()[8:]
                    sub_project = sub_project[:sub_project.index("<")]
                    f_path = dirname + "/" + sub_project
                    if os.path.exists(f_path + '/pom.xml') or os.path.exists(f_path + '/pom-template.xml'):
                        the_pom.write(line)
                else:
                    the_pom.write(line)
        os.chmod(dirname + '/pom.xml', 0444)
