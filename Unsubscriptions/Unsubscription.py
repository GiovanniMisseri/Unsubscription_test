import numpy as np
import pandas as pd
import argparse

def simulate_unsubscriptions_geom(n, p, T):
    '''
    Function to simulate the unsubscription journey for n costumers given a probability p of unsubcribing from the service.
    p stays constant for the whole number of observation windows T.
    '''
    unsubscriptions = np.random.geometric(p,n)-1 # draw n times from a geometric distribution with parameter p
    unsubscriptions[unsubscriptions>T] = T # cap the maximum occurence with the max observation time
    return unsubscriptions

def w_mean_estimator(renewal_time, print_stats=False):
    '''
    Estimation of the unsubscription probability by weighted mean.
    Take the ratio of unsubscriptions per time window and average over the T time windows giving each time window a weight proportional to its size.
    '''
    if int(max(renewal_time))==0:
        return 1
    perc_list = np.array([])
    prop_surv = np.array([])
    for i in range(int(max(renewal_time))):
        perc = sum(renewal_time==i)/sum(renewal_time>=i)
        perc_list = np.append(perc_list, perc)
        prop_surv = np.append(prop_surv, (sum(renewal_time>=i)/len(renewal_time))) # save the size of the population considered in the time window

    weight_list = prop_surv/np.sum(prop_surv) #normalize the weight
    stima_w_media = np.sum(perc_list*weight_list)
    if print_stats:
        print('stima media={}'.format(stima_w_media))
        print('rse media={}'.format(np.sqrt(np.square(p-stima_w_media))))
    return stima_w_media

parser = argparse.ArgumentParser()
parser.add_argument('--simulation_param_p', type=float, help='specify the probability of unsubscription per time window')
parser.add_argument('--simulation_param_n', type=int, help='specify the populazion size for the simulation')
parser.add_argument('--simulation_param_T', type=int, help='specify the observation period')
parser.add_argument('--output_path_simulation', type=str, help='specify the path where simulation data should be saved')

parser.add_argument('--path_input_data', type=str, help='path to the input data')
args = parser.parse_args()

#### SIMULATION ###
if (args.simulation_param_p is not None) & (args.simulation_param_n is not None) & (args.simulation_param_T is not None) & (args.output_path_simulation is not None):
    print('')
    print('starting Simulation')
    #set parameters
    p = args.simulation_param_p
    n = args.simulation_param_n
    T = args.simulation_param_T
    output_path = args.output_path_simulation

    #simulate data
    renewal_time = simulate_unsubscriptions_geom(n, p, T)

    #group results
    unique, counts = np.unique(renewal_time, return_counts=True)
    grouped_renewal = pd.DataFrame(unique, columns=['renewals'])
    grouped_renewal['T'] = T
    grouped_renewal['N'] = counts

    #save output
    grouped_renewal.to_csv(output_path,index=False)

### ESTIMATE ###
if args.path_input_data is not None:
    input_path = args.path_input_data
    dat = pd.read_csv(input_path)

    # reshape data to get one raw per observation
    dat_expand = dat.loc[dat.index.repeat(dat.N)].reset_index(drop=True)[['renewals', 'T']]

    # estimate parameter p
    p_dat = w_mean_estimator(dat_expand['renewals'])

    print('')
    print('The estimated parameter p in the provided data is: {}'.format(p_dat))

print('')
print('END')






