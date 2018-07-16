# N_of_data_entry  = 20000 (NODE) # de_cc_data.txt entry
NODE = 25
def index_list(list1,sorted_list):
    #print len(list1), len(sorted_list)
    index = []
    for i in range(len(sorted_list)) :
        ind = list1.index(sorted_list[i])
        index.append(ind)
    return index

def count_frequency( list1, item1 ) :
    s = 0
    for i in range(len(list1)) :
        if item1 == list1[i] :
            s += 1
    return s

def pharmacy_counting():
    # step 1 :
    data_c_dn_fn_ln_unit = []  # list for cost-drug name - first name - last name
    cost_data_unit = []
    data = open('./input/your_own_input_for_itcont.txt','r') # your_own_input_for_itcont.txt
    for i in range(NODE) :
        line = data.readline()
        lins_sp = line.split(',')
        if ( len(lins_sp) == 5 ) :
            cost_data_unit.append(lins_sp[4])
            data_c_dn_fn_ln_unit.append(line)  # checked for all records
    data.close()
    data_c_dn_fn_ln_unit.pop(0)
    cost_data_unit.pop(0)


    # step 2 :

    cost = []
    data_c_dn_fn_ln_unit_v1 = []
    for i in range(len(data_c_dn_fn_ln_unit)) :
        entry_split = data_c_dn_fn_ln_unit[i].split(',')
        cost.append(entry_split[4])
        data_c_dn_fn_ln_unit_v1.append( [[entry_split[1], entry_split[2]],entry_split[3] ])

    #print data_c_dn_fn_ln_unit_v1[0:5]


    # cost[] contains the cost list of all drugs for the unit. Now top_cost[]
    # need to be sorted for all the drugs in descending order along with their
    # indices so that corresponding drug_name can be identified, as well as
    # number of times a drug was prescribed for the same prescriber.

    # step 4 : sort drug_cost in descending order


    drug_cost = []
    for i in range(len(cost)) :
        c1 = float(cost[i])
        drug_cost.append(c1)
    drug_cost = list(set(drug_cost)) # added later
    drug_cost.sort(reverse = True)
    #print  'sorted drug_cost :', drug_cost[0:20]


    #print cost_data_unit[0:20]
    #print len(cost_data_unit), len(drug_cost)

    # convert items of cost_data_unit into float
    cost_data_unit_f = []
    for i in range( len(cost_data_unit) ) :
        c2 = float(cost_data_unit[i])
        cost_data_unit_f.append(c2)

    #print cost_data_unit_f
    index = index_list(cost_data_unit_f,drug_cost)
    #print index[0:10]

    # Now frequency of the top drugs that was prescribed multiple times
    # to same individual need to counted based on matching the
    # drug name and full name using data_c_dn_fn_ln_unit_v1 data

    # top_cost_drug.txt with drug_name,num_prescriber,total_cost


    top_drugs_prescriber = []
    for i in range(len(index)) :
        top_drugs_prescriber.append(data_c_dn_fn_ln_unit_v1[index[i]])
    #print top_drugs_prescriber[0:5]

    num_prescriber_rep = [] # No of times a person shares the drug
    for i in range(len(index)) :
        item = top_drugs_prescriber[i]
        freq = count_frequency( data_c_dn_fn_ln_unit_v1, item )
        num_prescriber_rep.append(freq)

    # print '\n'
    # print 'index : ', len(index), index[0:5]
    # print '\n'
    # print 'top_drugs_&_prescribers : ', len(top_drugs_prescriber), top_drugs_prescriber[0:5]
    # print'\n'
    # print 'num_of_prescriber : ', len(num_prescriber_rep), ', max value :', max(num_prescriber_rep), num_prescriber_rep[0:5]
    # print '\n'
    # print 'drug_cost : ', len(drug_cost), drug_cost[0:5]
    # print '\n'

    # top_cost_drug.txt need to be written as :
    # drug_name,num_prescriber,total_cost :
    # CHLORPROMAZINE,2,3000

    top_drug_name = []
    top_drug_cost = []
    for i in range( len(drug_cost) ) :
        top_drug_name.append(top_drugs_prescriber[i][1])
        c = int(round(drug_cost[i]))
        top_drug_cost.append(c)


    top_drug_name.insert(0, 'drug_name')
    num_prescriber_rep.insert(0, 'num_prescriber')
    top_drug_cost.insert(0, 'total_cost')
    #print top_drug_name, num_prescriber_rep, top_drug_cost

    # write output
    output = open('./output/top_cost_drug.txt','wb')
    for k in range( len(top_drug_name) ) :
        output.write( '%s%s%s%s%s\n' % (top_drug_name[k],',',num_prescriber_rep[k],',',str(top_drug_cost[k])) )
    output.close()

pharmacy_counting()
