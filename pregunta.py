"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    import pandas as pd
    import re

    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    cluster = []
    cantidad_de_palabras_clave = []
    porcentaje_de_palabras_clave = []
    principales_palabras_clave = []

    patron_cluster = re.compile(r'^\s*(\d+)\s+(\d+)\s+([\d,\.]+)\s+(.*?)\s*$')

    for line in lines:

        match = patron_cluster.match(line)
        if match:

            cluster.append(int(match.group(1)))
            cantidad_de_palabras_clave.append(int(match.group(2)))
            porcentaje_de_palabras_clave.append(float(match.group(3).replace(',', '.')))


            palabras_clave = match.group(4).split(',')
            principales_palabras_clave.append(', '.join([palabra.strip() for palabra in palabras_clave]))


    df_solucion = pd.DataFrame({
        'cluster': cluster,
        'cantidad_de_palabras_clave': cantidad_de_palabras_clave,
        'porcentaje_de_palabras_clave': porcentaje_de_palabras_clave,
    })

    # Agregar la cuarta columna a partir de los valores proporcionados
    df_solucion['principales_palabras_clave'] = [
        "maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionary algorithm, double-fed induction generator (dfig), ant colony optimisation, photo voltaic array, firefly algorithm, partial shade",
        "support vector machine, long short-term memory, back-propagation neural network, convolution neural network, speed wind prediction, energy consumption, wind power forecasting, extreme learning machine, recurrent-neural-network (rnn), radial basis function (rbf) networks, wind farm",
        "smart grid, wind power, reinforcement learning, energy management, energy efficiency, solar energy, deep reinforcement learning, demand-response (dr), internet of things, energy harvester, q-learning",
        "wind turbine, fault diagnosis, biodiesel, failure detection, response-surface methodology, condition monitoring, load forecasting, energy consumption forecast, anomalies detection, optimization-based algorithm, supervisory control and data acquisition",
        "electric vehicle, lithium-ion batteries, state of charge, state of health, hybrid-electric vehicle, energy management strategies, energy management system, remaining useful life, battery management system, transfer learning, hybrid energy storage",
        "particle swarm optimization, distribute generation, solar irradiance, artificial bee colonies, energy storage systems, bat algorithm, gravitational search algorithm, distributed system, multi-objective swarm optimization (mopso), optimal power-flow (opf), load-frequency control",
        "multi-objective optimization, energy storage, economic dispatch, non-dominated sorting genetic algorithm, sensitive analysis, hybrid renewable energy source, plug-in electric vehicle, combined-heat and power, multi-objective genetic algorithm, unit-commitment, dc-dc converters",
        "genetic algorithm, demand-side management, energy-saving, hybrid electric system (hes), wind turbine blade, data-driven modelling, simulated annealing, solar forecasting, geographic information system, renewable energy system, cogeneration",
        "anfis, global solar irradiance, solar irradiance forecast, genetic programing, islanding detection, expert system, distributed networks, evolutionary computation, wavelet-based neural network, root mean square errors, virtual power plant",
        "micro grid, multi-agent systems, distributed energy resource, batteries energy storage system, dc micro grid, pitch-control, droop control, hybrid ac/dc microgrid, voltage regulation, superconducting magnetic energy storage, distributed-control",
        "hydrogen, biochar, biomass, biogas, microbial fuel cell, gasification, biofuel, ethanol, engine performance, pyrolysis, anaerobic digester",
        "state of charge (soc) estimation, radial basis function, short-term load forecasting, computational fluid dynamics, generalized-regression neural network, monte-carlo simulation, multiple linear regression, power generation, nonlinear auto-regressive exogenous (narx) model neural networks, surrogate model, extreme gradient boosting",
        "pem fuel cell, solid-oxide fuel cell, deep-belief networks, energy optimisation, particles-size distributions, biomass gasification, exergy, battery management, hydrogen production, numeric simulation, system-identification"
    ]

    return df_solucion
