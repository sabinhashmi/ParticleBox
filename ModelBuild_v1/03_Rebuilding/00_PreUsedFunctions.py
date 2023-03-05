#In reference with 02_Composition.ipynb

# ----------------------------------------------------------------------------------------

## This cell can be avoided.

# track_type=['particle_isLong','particle_isLong_andUT','particle_isDown_noVelo']
# trackComposition = pd.DataFrame(track_type,columns=['Track Type'])
# true_count=[]
# false_count=[]
# for track in track_type:
#     false_count.append(data[track].value_counts()[0])
#     true_count.append(data[track].value_counts()[1])


# trackComposition['True Counts']=true_count
# trackComposition['False Counts']=false_count
# trackComposition['True Percentage']=trackComposition['True Counts']/(trackComposition['True Counts']+trackComposition['False Counts'])*100
# trackComposition['False Percentage']=trackComposition['False Counts']/(trackComposition['True Counts']+trackComposition['False Counts'])*100
# trackComposition


# ----------------------------------------------------------------------------------------

# # annotation of numbers in count plot.
# def countplots(column_name,plot_name,position):
#     plot_name=sns.countplot(data[column_name],ax=ax[position],palette='dark')
#     for p in plot_name.patches:
#             plot_name.annotate('{:.2e}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()-50))


# ----------------------------------------------------------------------------------------

# #Composition Check, order matters
# def compositionCheck():
#     trackType=[]
#     for index,row in data.iterrows():
#         # if (row['particle_isLong']==True) & (row['particle_hasUT']==True):
#         #     trackType.append('Long and UT')
        

#         if row['particle_isLong_andUT']==True:
#             trackType.append('Long Tracks')
        
#         elif row['particle_hasVelo']==True:
#             trackType.append('Velo Tracks')

#         elif row['particle_isDown_noVelo']==True:
#             trackType.append('Downstream Tracks')
#         else:
#             trackType.append('Other Tracks')
#     return trackType

# trackType=compositionCheck()
# data['trackType']=trackType

# ----------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------
# fig,ax=plt.subplots(1,3,figsize=(25,6))


# countplots('particle_hasVelo',plot_name='plot_1',position=0)
# countplots('particle_isDown_noVelo',plot_name='plot_2',position=1)
# countplots('particle_isLong_andUT',plot_name='plot_3',position=2)


# ----------------------------------------------------------------------------------------

# #Plotting the tracks counts.

# plt.figure(figsize=(12,8))
# plot=sns.countplot(trackType)
# for p in plot.patches:
#     plot.annotate('{:.2e}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()-50))

# plt.show()

# ----------------------------------------------------------------------------------------

#Dendrograms

# link=linkage(data.sample(frac=0.015))
# dendrogram(link)
# plt.show()


# data_scaled=minmax.fit_transform(data.sample(frac=0.015))


# link=linkage(data_scaled)
# dendrogram(link)
# plt.show()

# ----------------------------------------------------------------------------------------
