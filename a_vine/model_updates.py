"""
Fixes iDTR1278.xml model compartment naming.

For some reason, the model compartment is labeled as '_u' for all species.
Within the model, the BIGG ids add _* to each ID, ie, atp_p for periplasm.
So with the _u error, there would be atp_p_u, which throws off comparisons.
Fixing this plus exporting model, then will do a comparison between the
models to see what the differences are.
"""
from memote.suite.cli.reports import diff
import cobra
import os
import logging
from concerto.helpers.id_mappers import update_ids
from concerto.utils.biolog_help import add_biolog_exchanges


log = logging.getLogger()

_file_path = os.path.dirname(__file__)
starting_model_f_name = 'iDT1278.xml'
s_model_path = os.path.join(_file_path, starting_model_f_name)

starting_model = cobra.io.read_sbml_model(s_model_path)
starting_model.id = "AV"

output_model_name = 'azo_vine.xml'
output_model_path = os.path.join(_file_path, output_model_name)


def write_model(model):
    cobra.io.write_sbml_model(model, output_model_path)


def update_1(model):
    # updates bug in compartment of the model
    log.info("Updating compartments")
    for metabolite in model.metabolites:
        if metabolite.id[-2:] == "_u":
            # removes last two characters, namely "_u"
            metabolite.id = metabolite.id[:-2]
            # rename compartment
            metabolite.compartment = metabolite.id[-1]
    return model


def update_2(model):
    log.info('Adding annotations to metabolites')

    update_ids(model)
    return model


def update_3(model):
    # add missing biolog reactions to model
    log.info("Adding biolog exchange reactions to prefix")
    model = add_biolog_exchanges(model)
    return model


def update_model():
    # Fix compartments
    model = update_1(starting_model)
    model = update_2(model)
    model = update_3(model)
    write_model(model)


if __name__ == '__main__':
    update_model()
    model_paths = [s_model_path, output_model_path]
    diff(
        [
            *model_paths,
            '--filename', os.path.join(_file_path, 'model_differences.html')
         ]
    )
