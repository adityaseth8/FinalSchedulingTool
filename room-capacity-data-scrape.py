
rooms = pd.DataFrame(data[1:], columns=data[0])
rooms['Capacity'] = pd.to_numeric(rooms['Capacity'])  
rooms = rooms.sort_values('Capacity', ascending=False)
print(rooms)

# HTML format

# <div class="_user_table">
#    <table style="WIDTH:85%;">
#       <tbody> 
#          <tr> 
#              <td> 204 Art</td>
#              <td> 174 </td>
#              <td> hhdhd</td>
#              <td> hhdhfdf </td>
#          </tr>