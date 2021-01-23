LANG="en_US.UTF-8"
import math
import numpy as np
#import matplotlib.pyplot as plt
import ahkab
from ahkab import ahkab, circuit, time_functions


def toRad(val):
  return (float(val)/180)*math.pi


def calcAc(value,angle):
  #
  angle=toRad( float(angle))
  value=float(value)
  real = value*math.cos(angle)
  imag = value*math.sin(angle)
  return complex(real,imag)

def magnsqr(cmplx):
    return pow(cmplx.real , 2)+pow(cmplx.imag , 2)

def con(cmplx):
  return complex(cmplx.real,-cmplx.imag)


cho='y'
while cho=='y':

    mycircuit = circuit.Circuit(title="Circuits Project", filename=None)

    gnd = mycircuit.get_ground_node()
    

    fileName=""

    fileName=input("\nPlease Enter File Name(Without .txt) : ")
    outputFile=""
    outputFile=input("\nPlease Enter Output File Name(Without .txt) : ")
    outputFile=outputFile+".txt"


    fileName =fileName+".txt"

    file = open(fileName,"r")

    f=open(outputFile,"w")
   
    f.write("The output:")
    frequency=0
    ResArray=['']
    CurrentS=['']
    VoltageS=['']
    #
    CAP_ARR=['']
    INDUC_ARR=['']

    VCVS_ARR=['']
    VCCS_ARR=['']
    CCVS_ARR=['']
    CCCS_ARR=['']

    
    lines = file.readlines()
    
    for i in lines:
        thisline = i.split(" ")

        if thisline[0][0]=='V' or thisline[0][0]=='v':
            VoltageS=VoltageS+thisline

            if thisline[1]!='0' and thisline[2]!='0':
              mycircuit.add_vsource ( thisline[0] ,n1= thisline[1] ,n2= thisline[2],dc_value=0 ,ac_value= calcAc (thisline[3],thisline[4]))
            if thisline[2]=='0':
              mycircuit.add_vsource ( thisline[0] ,n1= thisline[1] ,n2= gnd,dc_value=0 ,ac_value= calcAc (thisline[3],thisline[4]))
            if thisline[1]=='0':
              mycircuit.add_vsource ( thisline[0] ,n1= gnd ,n2= thisline[2],dc_value=0 ,ac_value= calcAc (thisline[3],thisline[4]))
              


        if thisline[0][0]=='I' or thisline[0][0]=='i':
            
            CurrentS=CurrentS+thisline
            if thisline[1]!='0' and thisline[2]!='0':
              mycircuit.add_isource ( thisline[0] ,n1= thisline[1] ,n2= thisline[2],dc_value=0 ,ac_value= calcAc (thisline[3],thisline[4]))
            if thisline[2]=='0':
              mycircuit.add_isource ( thisline[0] ,n1= thisline[1] ,n2= gnd,dc_value=0 ,ac_value= calcAc (thisline[3],thisline[4]))
            if thisline[1]=='0':
              mycircuit.add_isource ( thisline[0] ,n1= gnd ,n2= thisline[2],dc_value=0 ,ac_value= calcAc (thisline[3],thisline[4]))

              
        if thisline[0][0]=='R' or  thisline[0][0]=='r':

             
             ResArray+=thisline
              
             if thisline[1]=='0':
                mycircuit.add_resistor(thisline [0] , n1=gnd, n2=thisline[2],value=float(thisline[3]))
            
             if thisline[2]=='0':
               mycircuit.add_resistor(thisline [0] , n1=thisline[1], n2=gnd,value=float(thisline[3]))
              
             if thisline[1]!='0' and thisline[2]!='0':
              mycircuit.add_resistor(thisline [0] , n1=thisline[1], n2=thisline[2],value=float(thisline[3]))
                        
        if thisline[0][0]=='L' or thisline[0][0]=='l':

            INDUC_ARR+=thisline
            
            if thisline[1]=='0':
                mycircuit.add_inductor(thisline [0] , n1=gnd, n2=thisline[2],value=float(thisline[3]))
            
            if thisline[2]=='0':
               mycircuit.add_inductor(thisline [0] , n1=thisline[1], n2=gnd,value=float(thisline[3]))
              
            if thisline[1]!='0' and thisline[2]!='0':
              mycircuit.add_inductor(thisline [0] , n1=thisline[1], n2=thisline[2],value=float(thisline[3]))
          
        if thisline[0][0]=='C' or thisline[0][0]=='c':
            
            
            CAP_ARR+=thisline
            
            if thisline[1]=='0':
                mycircuit.add_capacitor(thisline [0] , n1=gnd, n2=thisline[2],value=float(thisline[3]))
            
            if thisline[2]=='0':
               mycircuit.add_capacitor(thisline [0] , n1=thisline[1], n2=gnd,value=float(thisline[3]))
              
            if thisline[1]!='0' and thisline[2]!='0':
              mycircuit.add_capacitor(thisline[0], n1=thisline[1], n2=thisline[2],value=float(thisline[3]))
          
        if thisline[0][0]=='U' or thisline[0][0]=='u' :
              frequency=float(thisline[1])


        if thisline[0][0]=='E' or thisline[0][0]=='e':
          
            mycircuit.add_vcvs(thisline[0],n1=thisline[1],n2=thisline[2],sn1=thisline[4],sn2=thisline[3], value=float(thisline[5]))
            VCVS_ARR+=thisline


        if thisline[0][0]=='G' or thisline[0][0]=='g':
          
            mycircuit.add_vccs(thisline[0],n1=thisline[1],n2=thisline[2],sn1=thisline[3],sn2=thisline[4], value=float(thisline[5]))
            VCCS_ARR+=thisline

        if thisline[0][0]=='H' or thisline[0][0]=='h':
          
            CCVS_ARR+=thisline
           # mycircuit.remove_elem(thisline[2])
           # elem=mycircuit.get_elem_by_name(thisline[2])

        
           # if thisline[3]!='0' and thisline[4]!='0':
           #   mycircuit.add_vsource ( 'Hzerovolt'+thisline[0][1] ,n1= thisline[3] ,n2= thisline[4],dc_value=0 ,ac_value=0)
           # if thisline[4]=='0':
           #   mycircuit.add_vsource ( 'Hzerovolt'+thisline[0][1] ,n1= thisline[3] ,n2= gnd,dc_value=0 ,ac_value= 0)
           # if thisline[3]=='0':
             # mycircuit.add_vsource ( 'Hzerovolt'+thisline[0][1] ,n1= gnd ,n2= thisline[4],dc_value=0 ,ac_value= 0)
           

            mycircuit.add_ccvs(thisline[0],n1=thisline[1],n2=thisline[2],source_id='Hzerovolt'+thisline[0][1], value=float(thisline[5]))
            

        if thisline[0][0]=='F' or thisline[0][0]=='f':

            if thisline[3]!='0' and thisline[4]!='0':
              mycircuit.add_vsource ( 'zerovolt'+thisline[0][1] ,n1= thisline[3] ,n2= thisline[4],dc_value=0 ,ac_value= 0)
            if thisline[4]=='0':
              mycircuit.add_vsource ( 'zerovolt'+thisline[0][1] ,n1= thisline[3] ,n2= gnd,dc_value=0 ,ac_value= 0)
            if thisline[3]=='0':
              mycircuit.add_vsource ( 'zerovolt'+thisline[0][1] ,n1= gnd ,n2= thisline[4],dc_value=0 ,ac_value= 0)

            mycircuit.add_cccs(thisline[0],n1=thisline[1],n2=thisline[2],source_id='zerovolt'+thisline[0][1], value=float(thisline[5]))
            CCCS_ARR+=thisline
            
  
    
    ac = ahkab.new_ac(start=frequency,stop=frequency,points=0,x0=None)
    res = ahkab.run(mycircuit,ac)  
    myarr=res['ac'].keys()
   
    f.write('\n\n____________Active_Power____________\n\n')

    i=1
    while i <len(ResArray):
      node1='v'
      node2='v'
      value=0
      #
      f.write("\npow(")
      #
      f.write(ResArray[i]+')=')
      i=i+1
      node1=node1+ResArray[i]
      i=i+1
      node2=node2+ResArray[i]
      i=i+1
      value=float(ResArray[i])
      
      v1=0
      v2=0
      if node1 !='v0':
       v1= res['ac'] [node1]
       
      if node2 !='v0':
       v2= res['ac'] [node2]

      v=v2-v1
      v=magnsqr(v)
      #)
      temp=str(v/(2*value))
      f.write(temp)
      i=i+1

    f.write("\n\n____________Sources_Power____________\n\n")

    i=1
    while i < len(CurrentS):
      node1='v'
      node2='v'
      value=0
      phase=0
      #
      f.write("\npow(")
      #
      f.write(CurrentS[i]+')=')
      i=i+1
      node1=node1+CurrentS[i]
      i=i+1
      node2=node2+CurrentS[i]
      i=i+1
      value=float(CurrentS[i])
      i+=1
      phase=float(CurrentS[i])
      v1=0
      v2=0
      if node1 !='v0':
       v1= res['ac'] [node1]
       
      if node2 !='v0':
       v2= res['ac'] [node2]

      v=v2-v1
      pw=0.5*v*con(calcAc(value,phase))
      f.write(str(pw))
      i=i+1
    
    i=1
    while i < len(VoltageS):
      curr='I('
      value=0
      phase=0
      f.write("\npow(")
      f.write(VoltageS[i]+')=')
      curr+=VoltageS[i]+')'
      i=i+3
      value=float(VoltageS[i])
      i+=1
      phase=float(VoltageS[i])

      current= res['ac'] [curr]

      pw= (0.5)*calcAc(value,phase)*con(current)
      f.write(str(-pw))
      i=i+1


    i=1
    while i < len(CCCS_ARR):
        delatV=res['ac']['V'+CCCS_ARR[i+1]]-res['ac'] ['V'+CCCS_ARR[i+2]]
        currentthrough=con(float(CCCS_ARR[i+4])*(res['ac']['I('+'zerovolt'+CCCS_ARR[i][1]+')']))
        power=(0.5)*(delatV)*(con(currentthrough))
        f.write('\npow('+CCCS_ARR[i]+')='+str(power))
        i=i+6


    i=1
    while i < len(CCVS_ARR):
        delatV=float(CCVS_ARR[i+5])*(res['ac']['I('+'Hzerovolt'+CCVS_ARR[i][1]+')'])
        currentthrough=con(res['ac']['I('+CCVS_ARR[i]+')'])
        power=(0.5)*(delatV)*(con(currentthrough))
        f.write('\npow('+CCVS_ARR[i]+')='+str(power))
        i=i+6
      
        
    i=1
    while i < len(VCCS_ARR) :
        delatV= res['ac']['V'+VCCS_ARR[i+1]]-res['ac'] ['V'+VCCS_ARR[i+2]]
        currentthrough=con(float(VCCS_ARR[i+5])*((res['ac']['V'+str(i+3)])-(res['ac']['V'+str(i+4)])))
        power=0.5*delatV*con(currentthrough)
        f.write('\npow('+VCCS_ARR[i]+')='+str(power))
        i=i+6


    i=1
    while i < len(VCVS_ARR):
        delatV=res['ac']['V'+VCVS_ARR[i+1]]-res['ac'][VCVS_ARR[i+2]]
        currentthrough=res['ac']['I('+VCVS_ARR[i]+')']
        power=0.5*delatV*con(currentthrough)
        f.write('n\pow('+VCVS_ARR[i]+')='+str(power))
        i=i+6

    

    f.write("\n\n____________Reactive_Power____________\n\n")
    i=1
    while i < len(CAP_ARR) :
      node1='v'
      node2='v'
      value=0
      #
      f.write("\nReactive power(")
      #
      f.write(CAP_ARR[i]+')=')
      i=i+1
      node1=node1+CAP_ARR[i]
      i=i+1
      node2=node2+CAP_ARR[i]
      i=i+1
      value=1/(float(frequency*2*math.pi)*float(CAP_ARR[i])*complex(0,1))
      v1=0
      v2=0
               
      if node1 !='v0':
       v1= res['ac'] [node1]
       
      if node2 !='v0':
       v2= res['ac'] [node2]

      v=v2-v1
      v=magnsqr(v)
      power=v/(-2*value)
      temp=str(power.imag)
      f.write(temp)
      i=i+1


    i=1
    while i <len(INDUC_ARR):
      node1='v'
      node2='v'
      value=0
      #
      f.write("\nReactive power(")
      #
      f.write(INDUC_ARR[i]+')=')
      i=i+1
      node1=node1+INDUC_ARR[i]
      i=i+1
      node2=node2+INDUC_ARR[i]
      i=i+1
      value=frequency*2*math.pi*float(INDUC_ARR[i])*complex(0,1)

      v1=0
      v2=0
      if node1 !='v0':
       v1= res['ac'] [node1]
       
      if node2 !='v0':
       v2= res['ac'] [node2]

      v=v2-v1
      v=magnsqr(v)

      power=v/(-2*value)
      temp=str(power.imag)
      f.write(temp)
      i=i+1

   
    
    print (mycircuit)
    file.close()
    f.close()

    cho=input("\n Analyze another circuit ? y/n \n")