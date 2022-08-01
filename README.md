# Master-Thesis

As a result of climate change, wildfires become more dangerous, larger and more expensive than they ever have been before. Aerial firefighting is crucial for containing spreading wildfires. But it causes pilots to reach the limit of their skills. For risk prevention, airspace can be dedicated to fire fighting and temporary become closed for other traffic. As of course there can be no physical signposting mounted in the sky, knowing the when and where preflight is necessary for other pilots. This is achieved by a Notice-to-Airmissions- or NOTAM-system that issues temporary flight restrictions (abbreviated TFR) as short-term disaster site signposting. TFRs close the airspace for manned aircraft as well as for drones.
The goal of this study is to examine the relation between satellite-based fire observation data and restricted airspace for aerial firefighting to assess safety of the involved aircraft. The area of interest (AOI)is defined to be the 10 westerly U.S. FIRs. Fire cluster polygons from that AOI to be considered active fires are drawn from OroraTech´s Wildfire Service. A complete set of TFR texts from the Federal Aviation Administration FAA via online NOTAM Archive for the AOI is converted into GeoJSON format successfully, combining manual downloading with VBA, Power Queries and Python. Aircraft state vectors (aircraft locations) of aerial fire fighters are available since July of 2021. Thus, the examined time frame is chosen to be August until (and including) October 2021.
All gathered data is examined then to design workflows to answer questions of spatiotemporal relations. The time until a TFR is issued for a fire is considered as well as the TFRs´ spatial suitability for fighting spreading fires with airtankers. Finally, the state vectors of 59 fire fighting aircraft within the observed time frame are analyzed.
The workflows combining fire cluster and TFR polygons provide locations and times via both, fire cluster ids and TFR NOTAM numbers. These indicate potential cases where aerial firefighters may have had to work without a protective TFR dedicating the airspace to just firefighting. Incorporating aircraft locations as state vectors of actual fire fighting aircraft unveils true situations where these aircraft had to operate unsheltered. 13.4% of the aircraft movements are not flown in a safe environment. 42 of the 59 aircraft considered here are uncovered by a TFR at least once within the observed three months.
