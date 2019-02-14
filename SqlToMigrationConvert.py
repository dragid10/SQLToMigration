import os

import model
import model.Species
from model import Role, Migration, Source, Scheme, User


def create_migration_string(table_name, data):
    return """
     DB::table('{t_name}')->insert(
        array(
            {insert_data}
        )
    );
    """.format(t_name=table_name, insert_data=data).lstrip().rstrip()


def get_base_filename(filename):
    return os.path.basename(filename[0:filename.index(".")])


def create_migrations():
    f = open('sql/migrations.sql', 'r')
    migration_list = []
    for line in f:
        split_line = line.replace('(', '').replace(')', '').replace("'", "").split(',')
        migration_list.append(model.Migration.Migration(split_line[1].rstrip().lstrip()).__str__())

    out = open("out/" + get_base_filename(f.name) + "_migration", 'a', encoding="utf-8")
    for migration in migration_list:
        out.write(create_migration_string(get_base_filename(f.name), ''.join(migration.__str__())))


def create_roles():
    f = open('sql/roles.sql', 'r')
    role_list = []
    for line in f:
        split_line = line.replace('(', '').replace(')', '').replace("'", "").split(',')
        role_list.append(model.Role.Role(split_line[1].rstrip().lstrip()).__str__())

    out = open("out/" + get_base_filename(f.name) + "_migration", 'a', encoding="utf-8")
    for role in role_list:
        out.write(create_migration_string(get_base_filename(f.name), ''.join(role.__str__())))


def create_users():
    f = open('sql/users.sql', 'r')
    user_list = []
    for line in f:
        split_line = line.replace('(', '').replace(')', '').replace("'", "").split(',')
        user_list.append(model.User.User(
            split_line[1].rstrip().lstrip(),
            split_line[2].rstrip().lstrip(),
            split_line[3].rstrip().lstrip(),
            split_line[4].rstrip().lstrip(),
            split_line[5].rstrip().lstrip(),
            split_line[6].rstrip().lstrip(),
            split_line[7].rstrip().lstrip(),
            split_line[8].rstrip().lstrip(),
            split_line[9].rstrip().lstrip()
        ).__str__())

    out = open("out/" + get_base_filename(f.name) + "_migration", 'a', encoding="utf-8")
    for user in user_list:
        out.write(create_migration_string(get_base_filename(f.name), ''.join(user.__str__())))


def create_schemes():
    f = open('sql/schemes.sql', 'r')
    scheme_list = []
    for line in f:
        split_line = line.replace('(', '').replace(')', '').replace("'", "").split(',')
        scheme_list.append(model.Scheme.Scheme(split_line[1].rstrip().lstrip(), split_line[2].rstrip().lstrip(),
                                               split_line[3].rstrip().lstrip(), split_line[4].rstrip().lstrip(),
                                               split_line[7].rstrip().lstrip()).__str__())

    out = open("out/" + get_base_filename(f.name) + "_migration", 'a', encoding="utf-8")
    for scheme in scheme_list:
        out.write(create_migration_string(get_base_filename(f.name), ''.join(scheme.__str__())))


def create_sources():
    f = open('sql/sources.sql', 'r', encoding="utf-8")
    source_list = []
    for line in f:
        split_line = line.replace('(', '').replace(')', '').replace("'", "").split(',')
        source_list.append(model.Source.Source(split_line[1].rstrip().lstrip(), split_line[2].rstrip().lstrip(),
                                               split_line[3].rstrip().lstrip(), split_line[4].rstrip().lstrip(),
                                               split_line[5].rstrip().lstrip(), split_line[6].rstrip().lstrip(),
                                               split_line[7].rstrip().lstrip(), split_line[8].rstrip().lstrip(),
                                               split_line[9].rstrip().lstrip(),
                                               split_line[10].rstrip().lstrip()).__str__())

    out = open("out/" + get_base_filename(f.name) + "_migration", 'a', encoding="utf-8")
    for source in source_list:
        out.write(create_migration_string(get_base_filename(f.name), ''.join(source.__str__())))


def create_species():
    f = open('sql/species.sql', 'r', encoding="utf-8")
    species_list = []
    split_line = []
    for line in f:
        split_line.clear()
        split_line = line.replace('(', '').replace(')', '').replace("'", "").split(',')
        species_list.append(model.Species.Species(
            split_line[1].rstrip().lstrip(),
            split_line[2].rstrip().lstrip(),
            split_line[3].rstrip().lstrip(),
            split_line[5].rstrip().lstrip(),
            split_line[6].rstrip().lstrip(),
            split_line[7].rstrip().lstrip(),
            split_line[8].rstrip().lstrip(),
            split_line[13].rstrip().lstrip(),
            split_line[14].rstrip().lstrip(),
            split_line[15].rstrip().lstrip(),
            split_line[16].rstrip().lstrip(),
            split_line[17].rstrip().lstrip(),
            split_line[23].rstrip().lstrip(),
            split_line[24].rstrip().lstrip(),
            split_line[25].rstrip().lstrip(),
            split_line[27].rstrip().lstrip(),
            split_line[28].rstrip().lstrip(),
            split_line[29].rstrip().lstrip(),
            split_line[30].rstrip().lstrip(),
            split_line[31].rstrip().lstrip(),
            split_line[32].rstrip().lstrip(),
            split_line[33].rstrip().lstrip(),
            split_line[34].rstrip().lstrip(),
            split_line[35].rstrip().lstrip(),
            split_line[36].rstrip().lstrip(),
            split_line[37].rstrip().lstrip(),
            split_line[38].rstrip().lstrip(),
            split_line[39].rstrip().lstrip(),
            split_line[40].rstrip().lstrip(),
            split_line[42].rstrip().lstrip(),
            split_line[44].rstrip().lstrip(),
            split_line[45].rstrip().lstrip(),
            split_line[46].rstrip().lstrip(),
            split_line[47].rstrip().lstrip(),
            split_line[48].rstrip().lstrip(),
            split_line[49].rstrip().lstrip(),
            split_line[50].rstrip().lstrip(),
            split_line[51].rstrip().lstrip(),
            split_line[52].rstrip().lstrip(),
            split_line[53].rstrip().lstrip(),
            split_line[54].rstrip().lstrip(),
            split_line[55].rstrip().lstrip(),
            split_line[58].rstrip().lstrip(),
            split_line[59].rstrip().lstrip(),
            split_line[60].rstrip().lstrip(),
            split_line[61].rstrip().lstrip(),
            split_line[62].rstrip().lstrip(),
            split_line[67].rstrip().lstrip(),
            split_line[68].rstrip().lstrip()).__str__())

    out = open("out/" + get_base_filename(f.name) + "_migration", 'a', encoding="utf-8")
    for species in species_list:
        out.write(create_migration_string(get_base_filename(f.name), ''.join(species.__str__())))


if __name__ == '__main__':
    create_migrations()
    create_roles()
    create_schemes()
    create_sources()
    create_species()
    create_users()
