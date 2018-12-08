#part 1
#sum metadata records from data structure
day8input=open("input.txt")
input = day8input.readlines()[0].strip().split()
#
#read count nodes from list, starting at position, store their data in nodes and return where you are in the list when done
def read_nodes(list, position, count, nodes):
    parsed = 0
    index = position
    while parsed < count:
        #read from list
        num_children = int(list[index])
        num_metadata = int(list[index+1])
        index += 2
        current_node = len(nodes)
        nodes.append({'children':num_children,'metadata':[]})
        if num_children > 0:
            print current_node, num_children, num_metadata, index
            #if index > 100:
            #    break
            index = read_nodes(list,index,num_children, nodes)
        if num_metadata > 0:
            print 'reading metadata for node', current_node
            for metadata in list[index:index+num_metadata]:
                nodes[current_node]['metadata'].append(int(metadata))
            index += num_metadata
        parsed += 1
        
    return index

nodes = []

read_nodes(input, 0, 1, nodes)
   
#sum metadata
metadata_sum =  sum(sum(node['metadata']) for node in nodes)
#45868


#part 2
#find value of root node, where value of a node is the sum of the values of the children referenced in metadata, or the sum of the metadata if no children

def calc_value(values,refs):
    return sum(values[x-1] for x in refs if x < (len(values)+1))

def read_nodes_values(list, position, count, nodes):
    parsed = 0
    index = position
    values = [0 for x in range(count)]
    while parsed < count:
        #read from list
        num_children = int(list[index])
        num_metadata = int(list[index+1])
        index += 2
        current_node = len(nodes)
        nodes.append({'children':num_children,'metadata':[],'value':0})
        if num_children > 0:
            print current_node, num_children, num_metadata, index
            #if index > 100:
            #    break
            index, child_values = read_nodes_values(list,index,num_children, nodes)
        if num_metadata > 0:
            print 'reading metadata for node', current_node
            for metadata in list[index:index+num_metadata]:
                nodes[current_node]['metadata'].append(int(metadata))
            index += num_metadata
            #update value
            if num_children == 0:
                values[parsed] = sum(nodes[current_node]['metadata'])
            else:
                values[parsed] = calc_value(child_values,nodes[current_node]['metadata'])
                print 'with child values', child_values
            nodes[current_node]['value'] = values[parsed]
        parsed += 1
        
    return index, values

nodes = []

read_nodes_values(input, 0, 1, nodes)
#19724
