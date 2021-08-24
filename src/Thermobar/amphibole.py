import numpy as np
import matplotlib.pyplot as plt
from functools import partial
import inspect
import warnings as w
import numbers
import pandas as pd

from Thermobar.core import *


## Equations: Amphibole-only Barometers


def P_Kraw2012(T=None, *, Mgno_Amp, deltaNNO):
    '''
    Amphibole-only barometer (PH2O) from Krawczynski et al. (2012)

    **Note - this is only the pressure for the first appearance of amphibole,
    so should only be applied to the highest Mg# amphiboles in each suite.
    it also only gives the partial pressure of H2O, if there is CO2 in the system,
    this will not be equal to the total pressure.**
    '''

    return 0.01*((Mgno_Amp/52.7 -0.014*deltaNNO)**15.12)

def P_Ridolfi2012_1a(T=None, *, SiO2_Amp_13_cat, TiO2_Amp_13_cat, FeOt_Amp_13_cat,
                     MgO_Amp_13_cat, CaO_Amp_13_cat, K2O_Amp_13_cat, Na2O_Amp_13_cat, Al2O3_Amp_13_cat):
    '''
    Amphibole-only barometer: Equation 1a of Ridolfi and Renzulli (2012). Calibrated between 1.3-22 kbars
    '''
    return 0.01 * (np.exp(125.9332115 - 9.587571403 * SiO2_Amp_13_cat - 10.11615567 * TiO2_Amp_13_cat
    - 8.173455128 * Al2O3_Amp_13_cat- 9.226076274 * FeOt_Amp_13_cat - 8.793390507 * MgO_Amp_13_cat
    - 1.6658613 * CaO_Amp_13_cat + 2.48347198 * Na2O_Amp_13_cat + 2.519184959 * K2O_Amp_13_cat))


def P_Ridolfi2012_1b(T=None, *, SiO2_Amp_13_cat, TiO2_Amp_13_cat, FeOt_Amp_13_cat,
                     MgO_Amp_13_cat, CaO_Amp_13_cat, K2O_Amp_13_cat, Na2O_Amp_13_cat, Al2O3_Amp_13_cat):
    '''
    Amphibole-only barometer: Equation 1b of Ridolfi and Renzulli (2012). Calibrated between 1.3-5 kbars
    '''
    return (0.01 * (np.exp(38.722545085 - 2.695663047 * SiO2_Amp_13_cat - 2.35647038717941 * TiO2_Amp_13_cat
            - 1.30063975020919 * Al2O3_Amp_13_cat - 2.7779767369382 * FeOt_Amp_13_cat
            - 2.48384821395444 * MgO_Amp_13_cat- 0.661386638563983 * CaO_Amp_13_cat
            - 0.270530207793162 * Na2O_Amp_13_cat + 0.111696322092308 * K2O_Amp_13_cat)))


def P_Ridolfi2012_1c(T=None, *, SiO2_Amp_13_cat, TiO2_Amp_13_cat, FeOt_Amp_13_cat, MgO_Amp_13_cat,
                     CaO_Amp_13_cat, K2O_Amp_13_cat, Na2O_Amp_13_cat, Al2O3_Amp_13_cat):
    '''
    Amphibole-only barometer: Equation 1c of Ridolfi and Renzulli (2012). Calibrated between 1.3-5 kbars
    '''
    return (0.01 * (24023.367332 - 1925.298250* SiO2_Amp_13_cat
    - 1720.63250944418 * TiO2_Amp_13_cat - 1478.53847391822 * Al2O3_Amp_13_cat
    - 1843.19249824537 * FeOt_Amp_13_cat - 1746.94437497404 * MgO_Amp_13_cat
    - 158.279055907371 * CaO_Amp_13_cat - 40.4443246813322 * Na2O_Amp_13_cat
    + 253.51576430265 * K2O_Amp_13_cat))


def P_Ridolfi2012_1d(T=None, *, SiO2_Amp_13_cat, TiO2_Amp_13_cat, FeOt_Amp_13_cat, MgO_Amp_13_cat, CaO_Amp_13_cat,
                     K2O_Amp_13_cat, Na2O_Amp_13_cat, Al2O3_Amp_13_cat):
    '''
    Amphibole-only barometer: Equation 1d of Ridolfi and Renzulli (2012). . Calibrated between 4-15 kbars
    '''
    return (0.01 * (26105.7092067 - 1991.93398583468 * SiO2_Amp_13_cat
    - 3034.9724955129 * TiO2_Amp_13_cat - 1472.2242262718 * Al2O3_Amp_13_cat - 2454.76485311127 * FeOt_Amp_13_cat
    - 2125.79095875747 * MgO_Amp_13_cat - 830.644984403603 * CaO_Amp_13_cat
    + 2708.82902160291 * Na2O_Amp_13_cat + 2204.10480275638 * K2O_Amp_13_cat))


def P_Ridolfi2012_1e(T=None, *, SiO2_Amp_13_cat, TiO2_Amp_13_cat, FeOt_Amp_13_cat,
                     MgO_Amp_13_cat, CaO_Amp_13_cat, K2O_Amp_13_cat, Na2O_Amp_13_cat, Al2O3_Amp_13_cat):
    '''
    Amphibole-only barometer: Equation 1e of Ridolfi and Renzulli (2012).  Calibrated between 930-2200 kbars
    '''
    return (0.01 * np.exp(26.5426319326957 - 1.20851740386237 * SiO2_Amp_13_cat
    - 3.85930939071001 * TiO2_Amp_13_cat - 1.10536070667051 * Al2O3_Amp_13_cat
    - 2.90677947035468 * FeOt_Amp_13_cat - 2.64825741548332 *MgO_Amp_13_cat
    + 0.513357584438019 * CaO_Amp_13_cat
    + 2.9751971464851 * Na2O_Amp_13_cat + 1.81467032749331 * K2O_Amp_13_cat))


def P_Ridolfi2010(T=None, *, Al2O3_Amp_cat_23ox, cation_sum_Si_Ca):
    '''
    Amphibole-only (Al) barometer: Ridolfi et al. (2010)
    '''
    return (10 * (19.209 * np.exp(1.438 * Al2O3_Amp_cat_23ox *
            13 / cation_sum_Si_Ca)) / 1000)


def P_Hammerstrom1986_eq1(T=None, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Hammerstrom and Zen, 1986 eq.1
    '''
    return (-3.92 + 5.03 * Al2O3_Amp_cat_23ox)


def P_Hammerstrom1986_eq2(T=None, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Hammerstrom and Zen, 1986 eq.2
    '''
    return (1.27 * (Al2O3_Amp_cat_23ox**2.01))


def P_Hammerstrom1986_eq3(T=None, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Hammerstrom and Zen, 1986 eq.3
    '''
    return (0.26 * np.exp(1.48 * Al2O3_Amp_cat_23ox))


def P_Hollister1987(T=None, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Hollister et al. 1987
    '''
    return (-4.76 + 5.64 * Al2O3_Amp_cat_23ox)


def P_Johnson1989(T=None, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Johnson and Rutherford, 1989
    '''
    return (-3.46 + 4.23 * Al2O3_Amp_cat_23ox)


def P_Anderson1995(T, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Anderson and Smith (1995)
    '''
    return (4.76 * Al2O3_Amp_cat_23ox - 3.01 - (((T - 273.15 - 675) / 85)
            * (0.53 * Al2O3_Amp_cat_23ox + 0.005294 * (T - 273.15 - 675))))


def P_Blundy1990(T=None, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Blundy et al. 1990
    '''
    return (5.03 * Al2O3_Amp_cat_23ox - 3.53)


def P_Schmidt1992(T=None, *, Al2O3_Amp_cat_23ox):
    '''
    Amphibole-only (Al) barometer: Schmidt 1992
    '''
    return (-3.01 + 4.76 * Al2O3_Amp_cat_23ox)



## Function: Amphibole-only barometry

Amp_only_P_funcs = { P_Ridolfi2012_1a, P_Ridolfi2012_1b, P_Ridolfi2012_1c, P_Ridolfi2012_1d,
P_Ridolfi2012_1e, P_Ridolfi2010, P_Hammerstrom1986_eq1, P_Hammerstrom1986_eq2, P_Hammerstrom1986_eq3, P_Hollister1987,
P_Johnson1989, P_Blundy1990, P_Schmidt1992, P_Anderson1995, P_Kraw2012} # put on outside

Amp_only_P_funcs_by_name= {p.__name__: p for p in Amp_only_P_funcs}

def calculate_amp_only_melt_comps(amp_comps=None, equation=None, T_K=None):
    if equation=="Ridolfi21":
        amp_sites=calculate_sites_ridolfi(amp_comps=amp_comps)
        deltaNNO_calc= (-10.3216023230583*amp_sites['Al_IV_T'] + 4.47045484316415*amp_sites['Al_VI_C']
        + 7.55122550171372*amp_sites['Ti_C'] + 5.46318534905121*amp_sites['Fe3_C'] -4.73884449358073*amp_sites['Mg_C']
         -7.20328571556139*amp_sites['Fe2_C']-17.5610110666215*amp_sites['Mn_C'] + 13.762022684517*amp_sites['Ca_B']
         + 13.7560270877436*amp_sites['Na_A']  + 27.5944871599305*amp_sites['K_A'])
        amp_sites.insert(0, "deltaNNO_calc", deltaNNO_calc)

        H2O_calc=(np.exp(-1.374845602*amp_sites['Al_IV_T'] + 1.7103210931239*amp_sites['Al_VI_C']
        + 0.85944576818503*amp_sites['Ti_C'] + 1.18881568772057*amp_sites['Fe3_C'] -0.675980097369545*amp_sites['Mg_C']
         -0.390086849565756*amp_sites['Fe2_C']-6.40208103925722*amp_sites['Mn_C'] + 2.54899046000297*amp_sites['Ca_B']
         + 1.37094801209146*amp_sites['Na_A']  + 1.25720999388625*amp_sites['K_A']))
        amp_sites.insert(0, "H2O_calc", H2O_calc)
    if equation=="Zhang17":
        if T_K is None:
            w.warn('You must enter a value for T in Kelvin to get results from equation3')
        amp_sites=get_amp_sites_avferric_zhang(amp_comps=amp_comps)

        amp_sites['SiO2_Eq1']=(-736.7170+288.733*np.log(amp_sites['Si_T_ideal'])+56.536*amp_sites['Al_VI_C_ideal']
        +27.169*(amp_sites['Mg_C_ideal']+amp_sites['Mg_B_ideal'])
+ 62.665*amp_sites['Fe3_C_ideal']+34.814*(amp_sites['Fe2_C_ideal']+amp_sites['Fe2_B_ideal'])
+83.989*(amp_sites['Ti_T_ideal']+amp_sites['Ti_C_ideal'])+44.225*amp_sites['Ca_B_ideal']+14.049*amp_sites['Na_A_ideal'])

        amp_sites['SiO2_Eq2']=(-399.9891 + 212.9463*np.log(amp_sites['Si_T_ideal']) + 11.7464*amp_sites['Al_VI_C_ideal'] +
        23.5653*amp_sites['Fe3_C_ideal'] + 6.8467*(amp_sites['Fe2_C_ideal']+amp_sites['Fe2_B_ideal']) +
        24.7743*(amp_sites['Ti_T_ideal']+amp_sites['Ti_C_ideal']) + 24.4399 * amp_sites['Ca_B_ideal'])

        amp_sites['SiO2_Eq4']=(-222.614 + 167.517*np.log(amp_sites['Si_T_ideal']) -7.156*(amp_sites['Mg_C_ideal']
        +amp_sites['Mg_B_ideal']))

        amp_sites['TiO2_Eq6']=(np.exp(22.4650  -2.5975*amp_sites['Si_T_ideal']
            -1.15502*amp_sites['Al_VI_C_ideal'] -2.23287*amp_sites['Fe3_C_ideal'] -1.03193*(amp_sites['Fe2_C_ideal']+amp_sites['Fe2_B_ideal'])
            -1.98253*amp_sites['Ca_B_ideal']-1.55912*amp_sites['Na_A_ideal']))

        amp_sites['FeO_Eq7']=(np.exp(24.4613  -2.72308*amp_sites['Si_T_ideal']
            -1.07345*amp_sites['Al_VI_C_ideal'] -1.0466*amp_sites['Fe3_C_ideal'] -0.25801*(amp_sites['Fe2_C_ideal']+amp_sites['Fe2_B_ideal'])
            -1.93601*amp_sites['Ti_C_ideal']-2.52281*amp_sites['Ca_B_ideal']))

        amp_sites['FeO_Eq8']=(np.exp(15.6864  -2.09657*amp_sites['Si_T_ideal']
           +0.36457*amp_sites['Mg_C_ideal'] -1.33131*amp_sites['Ca_B_ideal']))

        amp_sites['MgO_Eq9']=(np.exp(12.6618  -2.63189*amp_sites['Si_T_ideal']
           +1.04995*amp_sites['Al_VI_C_ideal'] +1.26035*amp_sites['Mg_C_ideal']))

        amp_sites['CaO_Eq10']=(41.2784  -7.1955*amp_sites['Si_T_ideal']
           +3.6412*amp_sites['Mg_C_ideal'] -5.0437*amp_sites['Na_A_ideal'])

        amp_sites['CaO_Eq11']=np.exp((6.4192  -1.17372*amp_sites['Si_T_ideal']
           +1.31976*amp_sites['Al_VI_C_ideal'] +0.67733*amp_sites['Mg_C_ideal']))

        amp_sites['K2O_Eq12']=(100.5909  -4.3246*amp_sites['Si_T_ideal']
            -17.8256*amp_sites['Al_VI_C_ideal']-10.0901*amp_sites['Mg_C_ideal'] -15.683*amp_sites['Fe3_C_ideal']
            -8.8004*(amp_sites['Fe2_C_ideal']+amp_sites['Fe2_B_ideal'])-19.7448*amp_sites['Ti_C_ideal']
            -6.3727*amp_sites['Ca_B_ideal']-5.8069*amp_sites['Na_A_ideal'])

        amp_sites['K2O_Eq13']=(-16.53  +1.6878*amp_sites['Si_T_ideal']
            +1.2354*(amp_sites['Fe3_C_ideal']+amp_sites['Fe2_C_ideal']+amp_sites['Fe2_B_ideal'])
            +5.0404*amp_sites['Ti_C_ideal']+2.9703*amp_sites['Ca_B_ideal'])

        amp_sites['Al2O3_Eq14']=(4.573 + 6.9408*amp_sites['Al_VI_C_ideal']+1.0059*amp_sites['Mg_C_ideal']
         +4.5448*amp_sites['Fe3_C_ideal']+5.9679*amp_sites['Ti_C_ideal']
            +7.1501*amp_sites['Na_A_ideal'])


        if T_K is not None:
            amp_sites['SiO2_Eq3']=(-228 + 0.01065*(T_K-273.15) + 165*np.log(amp_sites['Si_T_ideal'])
            -7.219*(amp_sites['Mg_C_ideal']+amp_sites['Mg_B_ideal']))

            amp_sites['TiO2_Eq5']=(np.exp( 23.4870 -0.0011*(T_K-273.15) +-2.5692*amp_sites['Si_T_ideal']
            -1.3919*amp_sites['Al_VI_C_ideal'] -2.1195361*amp_sites['Fe3_C_ideal'] -1.0510775*(amp_sites['Fe2_C_ideal']+amp_sites['Fe2_B_ideal'])
            -2.0634034*amp_sites['Ca_B_ideal']-1.5960633*amp_sites['Na_A_ideal']))




        return amp_sites



def calculate_amp_only_press(amp_comps=None, equationP=None, T=None, deltaNNO=None):
    """
    Amphibole-only barometry, returns pressure in kbar.

    amp_comps: DataFrame
        Amphibole compositions with column headings SiO2_Amp, MgO_Amp etc.


    EquationP: str
        | P_Mutch2016 (T-independent)
        | P_Ridolfi2012_1a (T-independent)
        | P_Ridolfi2012_1b (T-independent)
        | P_Ridolfi2012_1c (T-independent)
        | P_Ridolfi2012_1d (T-independent)
        | P_Ridolfi2012_1e (T-independent)
        | P_Ridolfi2021 - (T-independent)- Uses new algorithm in 2021 paper to
        select pressures from equations 1a-e.

        | P_Ridolfi2010  (T-independent)
        | P_Hammerstrom1986_eq1  (T-independent)
        | P_Hammerstrom1986_eq2 (T-independent)
        | P_Hammerstrom1986_eq3 (T-independent)
        | P_Hollister1987 (T-independent)
        | P_Johnson1989 (T-independent)
        | P_Blundy1990 (T-independent)
        | P_Schmidt1992 (T-independent)
        | P_Anderson1995 (*T-dependent*)

    T: float, int, series, str  ("Solve")
        Temperature in Kelvin
        Only needed for T-sensitive barometers.
        If enter T="Solve", returns a partial function
        Else, enter an integer, float, or panda series

    Returns
    -------
    pandas series
       Pressure in kbar
    """
    if equationP !="P_Ridolfi2021" and equationP !="P_Mutch2016":
        try:
            func = Amp_only_P_funcs_by_name[equationP]
        except KeyError:
            raise ValueError(f'{equationP} is not a valid equation') from None
        sig=inspect.signature(func)

        if sig.parameters['T'].default is not None:
            if T is None:
                raise ValueError(f'{equationP} requires you to enter T, or specify T="Solve"')
        else:
            if T is not None:
                print('Youve selected a T-independent function')

        if isinstance(T, pd.Series):
            if amp_comps is not None:
                if len(T) != len(amp_comps):
                    raise ValueError('The panda series entered for Temperature isnt the same length as the dataframe of amphibole compositions')

    if equationP == "P_Kraw2012":
        w.warn('This barometer gives the PH2O for the first appearance of'
        ' amphibole. It should only be applied to the highest Mg# in each'
        ' sample suite. Note, if there is CO2 in the system P=/ PH2O')
        if deltaNNO is None:
            raise ValueError('P_Kraw2012 requires you to enter a deltaNNO value')
        Mgno_Amp=100*(amp_comps['MgO_Amp']/40.3044)/((amp_comps['MgO_Amp']/40.3044)+(amp_comps['FeOt_Amp']/71.844))
        P_kbar=P_Kraw2012(Mgno_Amp=Mgno_Amp,
        deltaNNO=deltaNNO)
        df_out=pd.DataFrame(data={'PH2O_kbar_calc': P_kbar,
        'Mg#_Amp': Mgno_Amp})
        return df_out


    if "Sample_ID_Amp" not in amp_comps:
        amp_comps['Sample_ID_Amp'] = amp_comps.index

    if equationP == "P_Mutch2016":
        ox23 = calculate_23oxygens_amphibole(amp_comps)
        Amp_sites_initial = get_amp_sites_mutch(ox23)
        norm_cat = amp_components_ferric_ferrous_mutch(Amp_sites_initial, ox23)
        final_cat = get_amp_sites_ferric_ferrous_mutch(norm_cat)
        final_cat['Al_tot'] = final_cat['Al_T'] + final_cat['Al_C']
        P_kbar = 0.5 + 0.331 * \
            final_cat['Al_tot'] + 0.995 * (final_cat['Al_tot'])**2
        final_cat.insert(0, "P_kbar_calc", P_kbar)
        return final_cat

    if 'Ridolfi2012' in equationP or equationP == "P_Ridolfi2021":

        cat13 = calculate_13cations_amphibole_ridolfi(amp_comps)

        myAmps1_label = amp_comps.drop(['Sample_ID_Amp'], axis='columns')
        Sum_input = myAmps1_label.sum(axis='columns')

        kwargs_1a = {name: cat13[name] for name, p in inspect.signature(
            P_Ridolfi2012_1a).parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}
        kwargs_1b = {name: cat13[name] for name, p in inspect.signature(
            P_Ridolfi2012_1b).parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}
        kwargs_1c = {name: cat13[name] for name, p in inspect.signature(
            P_Ridolfi2012_1c).parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}
        kwargs_1d = {name: cat13[name] for name, p in inspect.signature(
            P_Ridolfi2012_1d).parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}
        kwargs_1e = {name: cat13[name] for name, p in inspect.signature(
            P_Ridolfi2012_1e).parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}

        P_MPa_1a = 100 * partial(P_Ridolfi2012_1a, **kwargs_1a)(0)
        P_MPa_1b = 100 * partial(P_Ridolfi2012_1b, **kwargs_1b)(0)
        P_MPa_1c = 100 * partial(P_Ridolfi2012_1c, **kwargs_1c)(0)
        P_MPa_1d = 100 * partial(P_Ridolfi2012_1d, **kwargs_1d)(0)
        P_MPa_1e = 100 * partial(P_Ridolfi2012_1e, **kwargs_1e)(0)

        if equationP == "P_Ridolfi2021":


            XPae = (P_MPa_1a - P_MPa_1e) / P_MPa_1a
            deltaPdb = P_MPa_1d - P_MPa_1b

            P_MPa = np.empty(len(P_MPa_1a))
            name=np.empty(len(P_MPa_1a), dtype=np.dtype('U100'))
            for i in range(0, len(P_MPa_1a)):
                if P_MPa_1b[i] < 335:
                    P_MPa[i] = P_MPa_1b[i]
                    name[i]="1b"
                elif P_MPa_1b[i] < 399:
                    P_MPa[i] = (P_MPa_1b[i] + P_MPa_1c[i]) / 2
                    name[i]="(1b+1c)/2"
                elif P_MPa_1c[i] < 415:
                    P_MPa[i] = (P_MPa_1c[i])
                    name[i]="1c"
                elif P_MPa_1d[i] < 470:
                    P_MPa[i] = (P_MPa_1c[i])
                    name[i]="1c"
                elif XPae[i] > 0.22:
                    P_MPa[i] = (P_MPa_1c[i] + P_MPa_1d[i]) / 2
                    name[i]="1c+1d"
                elif deltaPdb[i] > 350:
                    P_MPa[i] = P_MPa_1e[i]
                    name[i]="1e"
                elif deltaPdb[i] > 210:
                    P_MPa[i] = P_MPa_1d[i]
                    name[i]="1d"
                elif deltaPdb[i] < 75:
                    P_MPa[i] = P_MPa_1c[i]
                    name[i]="1c"
                elif XPae[i] < -0.2:
                    P_MPa[i] = (P_MPa_1b[i] + P_MPa_1c[i]) / 2
                    name[i]="(1b+1c)/2"
                elif XPae[i] > 0.05:
                    P_MPa[i] = (P_MPa_1c[i] + P_MPa_1d[i]) / 2
                    name[i]="(1c+1d)/2"
                else:
                    P_MPa[i] = P_MPa_1a[i]
                    name[i]="1a"
                if Sum_input[i] < 90:
                    P_MPa[i] = np.nan

            # P_kbar = pd.DataFrame(data={"P_kbar_calc": (P_MPa / 100), "equation": name,
            # "H2O":Calcs_R['H2O_calc']})

        Calcs_R=cat13.copy()
        Calcs_R['P_kbar_calc']=P_MPa / 100
        Calcs_R['equation']=name
        Calcs_R['Sum_input']=Sum_input
        Low_sum=Sum_input<90
        Calcs_R['H2O_calc']=(2-cat13['F_Amp_13_cat']-cat13['Cl_Amp_13_cat'])*cat13['cation_sum_Si_Mg']*17/13/2
        Calcs_R.loc[(Low_sum), 'H2O_calc']=np.nan

        Calcs_R['Charge']=(cat13['SiO2_Amp_13_cat']*4+cat13['TiO2_Amp_13_cat']*4+cat13['Al2O3_Amp_13_cat']*3+
        cat13['Cr2O3_Amp_13_cat']*3+cat13['FeOt_Amp_13_cat']*2+cat13['MnO_Amp_13_cat']*2+cat13['MgO_Amp_13_cat']*2
        +cat13['CaO_Amp_13_cat']*2+cat13['Na2O_Amp_13_cat']+cat13['K2O_Amp_13_cat'])

         #BJ3>60
        Calcs_R['APE']=np.abs(P_MPa_1a-P_MPa)/(P_MPa_1a+P_MPa)*200
        High_APE=Calcs_R['APE']>60
        Calcs_R.loc[(High_APE), 'Input_Check']=False
        Calcs_R.loc[(High_APE), 'Fail Msg']="APE >60"

        # If DG2 (charge)>46, set Fe3 to zero, else set to 46-charge
        Calcs_R['Fe3_calc']=46-Calcs_R['Charge']
        High_Charge=Calcs_R['Charge']>46
        Calcs_R.loc[(High_Charge), 'Fe3_calc']=0

        Calcs_R['Fe2_calc']=cat13['FeOt_Amp_13_cat']-Calcs_R['Fe3_calc']


        Calcs_R['Fe2O3_calc']=Calcs_R['Fe3_calc']*cat13['cation_sum_Si_Mg']*159.691/13/2
        Calcs_R.loc[(Low_sum), 'Fe2O3_calc']=np.nan

        Calcs_R['FeO_calc']=Calcs_R['Fe2_calc']*cat13['cation_sum_Si_Mg']*71.846/13
        Calcs_R.loc[(Low_sum), 'Fe2O3_calc']=np.nan

        Calcs_R['O=F,Cl']=-(amp_comps['F_Amp']*0.421070639014633+amp_comps['Cl_Amp']*0.225636758525372)
        Calcs_R.loc[(Low_sum), 'O=F,Cl']=np.nan

        Calcs_R['Total_recalc']=(Sum_input-amp_comps['FeOt_Amp']+Calcs_R['H2O_calc']+Calcs_R['Fe2O3_calc']
        +Calcs_R['FeO_calc']+Calcs_R['O=F,Cl'])
        Calcs_R.loc[(Low_sum), 'Total']=np.nan

        # Set up a column for a fail message
        Calcs_R['Fail Msg']=""
        Calcs_R['Input_Check']=True

        # Check that old total isn't <90

        Calcs_R.loc[(Low_sum), 'Input_Check']=False
        Calcs_R.loc[(Low_sum), 'Fail Msg']="Cation oxide Total<90"

        # First check, that new total is >98.5 (e.g with recalculated H2O etc).

        Low_total_Recalc=Calcs_R['Total_recalc']<98.5
        Calcs_R.loc[(Low_total_Recalc), 'Input_Check']=False
        Calcs_R.loc[(Low_total_Recalc), 'Fail Msg']="Recalc Total<98.5"

        # Next, check that new total isn't >102
        High_total_Recalc=Calcs_R['Total_recalc']>102
        Calcs_R.loc[(High_total_Recalc), 'Input_Check']=False
        Calcs_R.loc[(High_total_Recalc), 'Fail Msg']="Recalc Total>102"

        # Next, check that charge isn't >46.5 ("unbalanced")
        Unbalanced_Charge=Calcs_R['Charge']>46.5
        Calcs_R.loc[(Unbalanced_Charge), 'Input_Check']=False
        Calcs_R.loc[(Unbalanced_Charge), 'Fail Msg']="unbalanced charge (>46.5)"

        # Next check that Fe2+ is greater than 0, else unbalanced
        Negative_Fe2=Calcs_R['Fe2_calc']<0
        Calcs_R.loc[(Negative_Fe2), 'Input_Check']=False
        Calcs_R.loc[(Negative_Fe2), 'Fail Msg']="unbalanced charge (Fe2<0)"

        # Check that Mg# calculated using just Fe2 is >54, else low Mg
        Calcs_R['Mgno_Fe2']=cat13['MgO_Amp_13_cat']/(cat13['MgO_Amp_13_cat']+Calcs_R['Fe2_calc'])
        Low_Mgno=100*Calcs_R['Mgno_Fe2']<54
        Calcs_R.loc[(Low_Mgno), 'Input_Check']=False
        Calcs_R.loc[(Low_Mgno), 'Fail Msg']="Low Mg# (<54)"

        #Only ones that matter are low Ca, high Ca, BJ3>60, low B cations"



        # If Column CU<1.5,"low Ca"
        Ca_low=cat13['CaO_Amp_13_cat']<1.5
        Calcs_R.loc[(Ca_low), 'Input_Check']=False
        Calcs_R.loc[(Ca_low), 'Fail Msg']="Low Ca (<1.5)"

        # If Column CU>2.05, "high Ca"
        Ca_high=cat13['CaO_Amp_13_cat']>2.05
        Calcs_R.loc[(Ca_high), 'Input_Check']=False
        Calcs_R.loc[(Ca_high), 'Fail Msg']="High Ca (>2.05)"

        # Check that CW<1.99, else "Low B cations"
        Calcs_R['Na_calc']=2-cat13['CaO_Amp_13_cat']
        Ca_greaterthanNa=cat13['Na2O_Amp_13_cat']<(2-cat13['CaO_Amp_13_cat'])
        Calcs_R.loc[(Ca_greaterthanNa), 'Na_calc']=cat13['Na2O_Amp_13_cat']
        Calcs_R['B_Sum']=Calcs_R['Na_calc']+cat13['CaO_Amp_13_cat']

        Low_B_Cations=Calcs_R['B_Sum']<1.99
        Calcs_R.loc[(Low_B_Cations), 'Input_Check']=False
        Calcs_R.loc[(Low_B_Cations), 'Fail Msg']="Low B Cations"


         #P_MPa
        Failed_input=Calcs_R['Input_Check']==False
        Calcs_R.loc[Failed_input, 'P_kbar_calc']=np.nan

        cols_to_move = ['P_kbar_calc', 'Input_Check', "Fail Msg",
                        'equation', 'H2O_calc', 'Fe2O3_calc', 'FeO_calc', 'Total_recalc', 'Sum_input']
        Calcs_R= Calcs_R[cols_to_move +
                                        [col for col in Calcs_R.columns if col not in cols_to_move]]



        # Check that CU>2.05, else high Ca


        # Check that DK2>0.25, else "high Al#"



        # Check that I2<38.8-0.42, else Low SiO2



        # If I2>49.8, high SiO2


        # IF  CI2>0.06+0.06*0.2,"high-[4]Ti


        # If CL2>0.57+0.57*0.074,"high-[6]Al


        # If CM2>0.7+0.7*0.07,"high-[6]Ti"


        # If CN2>0.04+0.04*0.1,"high-Cr2O3


        # If CO2>1.37+1.37*0.28,"high-Fe3+"


        # If O2<9.71-0.35,"low-MgO"


        # If O2>18.01+0.35,"high-MgO"

        # If CQ2>1.69+1.69*0.28,"high-Fe2+"

        # If N2>0.58+0.58*0.3,"high-MnO"

        # If (P2>12.35+0.25,"high-CaO"

        # If CY2<0,"low-ANa"


        #  IF IF(CY2>0.58+0.58*0.11,"high-ANa"


        # If R2<0,"low-K2O"

        # If R2>2.03+0.05,"high-K2O"

        # If DA2<0.03-0.03*0.3,"low-A(Na+K)

        # If DA2>1,"high-A(Na+K)"

        # If K2<6.5,"low-Al2O3

        #  If K2>15.9+0.36,"high-Al2O3"

        # If J2<1.1-0.2,"low-TiO2"

        # If M2<5.85-0.44,"low-FeO"

        # If M2>16.92+0.44,"high-FeO

        # If Q2<1.07-0.1,"low-Na2O

        # Q2>3.05+0.1,"high-Na2O

        # But to print "wrong", is looking 1) If "low Total", "high total", "unbalanced", "low Mg", "low Ca",
        # high Ca, BJ2>60, "low B cations".






        return Calcs_R # was P_kbar

        if equationP == "P_Ridolfi2012_1a":
            P_kbar = P_MPa_1a / 100
            return P_kbar

        if equationP == "P_Ridolfi2012_1b":
            P_kbar = P_MPa_1b / 100
            return P_kbar

        if equationP == "P_Ridolfi2012_1c":
            P_kbar = P_MPa_1c / 100
            return P_kbar

        if equationP == "P_Ridolfi2012_1d":
            P_kbar = P_MPa_1d / 100
            return P_kbar

        if equationP == "P_Ridolfi2012_1e":
            P_kbar = P_MPa_1e / 100
            return P_kbar



    if equationP != "Mutch2016" and 'Ridolfi2012' not in equationP and equationP != "P_Ridolfi2021":
        ox23_amp = calculate_23oxygens_amphibole(amp_comps=amp_comps)

    kwargs = {name: ox23_amp[name] for name, p in sig.parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}
    if isinstance(T, str) or T is None:
        if T == "Solve":
            P_kbar = partial(func, **kwargs)
        if T is None:
            P_kbar=func(**kwargs)

    else:
        P_kbar=func(T, **kwargs)

    return P_kbar

def calculate_amp_only_press_all_eqs(amp_comps, plot=False, H2O_Liq=None):
    import warnings
    with w.catch_warnings():
        w.simplefilter('ignore')
        amp_comps_c=get_amp_sites_from_input(amp_comps=amp_comps)
        amp_comps_c['P_Ridolfi21']=calculate_amp_only_press(amp_comps=amp_comps, equationP="P_Ridolfi2021").P_kbar_calc
        X_Ridolfi21_Sorted=np.sort(amp_comps_c['P_Ridolfi21'])
        if plot==True:
            plt.step(np.concatenate([X_Ridolfi21_Sorted, X_Ridolfi21_Sorted[[-1]]]),
            np.arange(X_Ridolfi21_Sorted.size+1)/X_Ridolfi21_Sorted.size, color='blue', linewidth=1,
            label="Ridolfi21")



    return amp_comps_c

## Amphibole-only thermometers


def T_Put2016_eq5(P=None, *, SiO2_Amp_cat_23ox,
                  TiO2_Amp_cat_23ox, FeOt_Amp_cat_23ox, Na2O_Amp_cat_23ox):
    '''
    Amphibole-only thermometer: Equation 5 of Putirka et al. (2016)
    '''
    return (273.15 + 1781 - 132.74 * SiO2_Amp_cat_23ox + 116.6 *
            TiO2_Amp_cat_23ox - 69.41 * FeOt_Amp_cat_23ox + 101.62 * Na2O_Amp_cat_23ox)


def T_Put2016_eq6(P, *, SiO2_Amp_cat_23ox,
                  TiO2_Amp_cat_23ox, FeOt_Amp_cat_23ox, Na2O_Amp_cat_23ox):
    '''
    Amphibole-only thermometer: Equation 6 of Putirka et al. (2016)
    '''
    return (273.15 + 1687 - 118.7 * SiO2_Amp_cat_23ox + 131.56 * TiO2_Amp_cat_23ox -
            71.41 * FeOt_Amp_cat_23ox + 86.13 * Na2O_Amp_cat_23ox + 22.44 * P / 10)


def T_Put2016_SiHbl(P=None, *, SiO2_Amp_cat_23ox):
    '''
    Amphibole-only thermometer: Si in Hbl, Putirka et al. (2016)
    '''
    return (273.15 + 2061 - 178.4 * SiO2_Amp_cat_23ox)

def T_Ridolfi2012(P, *, SiO2_Amp_13_cat, TiO2_Amp_13_cat, FeOt_Amp_13_cat,
                  MgO_Amp_13_cat, CaO_Amp_13_cat, K2O_Amp_13_cat, Na2O_Amp_13_cat, Al2O3_Amp_13_cat):
    '''
    Amphibole-only thermometer of Ridolfi and Renzuli, 2012
    '''
    return (273.15 + 8899.682 - 691.423 * SiO2_Amp_13_cat - 391.548 * TiO2_Amp_13_cat - 666.149 * Al2O3_Amp_13_cat
    - 636.484 * FeOt_Amp_13_cat -584.021 * MgO_Amp_13_cat - 23.215 * CaO_Amp_13_cat
    + 79.971 * Na2O_Amp_13_cat - 104.134 * K2O_Amp_13_cat + 78.993 * np.log(P * 100))

def T_Put2016_eq8(P, *, SiO2_Amp_cat_23ox, TiO2_Amp_cat_23ox,
                  MgO_Amp_cat_23ox, Na2O_Amp_cat_23ox):
    '''
    Amphibole-only thermometer: Eq8,  Putirka et al. (2016)
    '''
    return (273.15+1201.4 - 97.93 * SiO2_Amp_cat_23ox + 201.82 * TiO2_Amp_cat_23ox +
            72.85 * MgO_Amp_cat_23ox + 88.9 * Na2O_Amp_cat_23ox + 40.65 * P / 10)
## Equations: Amphibole-Liquid barometers

def P_Put2016_eq7a(T=None, *, Al2O3_Amp_cat_23ox, Na2O_Amp_cat_23ox,
K2O_Amp_cat_23ox, Al2O3_Liq_mol_frac_hyd, Na2O_Liq_mol_frac_hyd,
H2O_Liq_mol_frac_hyd, P2O5_Liq_mol_frac_hyd):
    '''
    Amphibole-Liquid barometer: Equation 7a of Putirka et al. (2016)
    '''
    return (10 * (-3.093 - 4.274 * np.log(Al2O3_Amp_cat_23ox / Al2O3_Liq_mol_frac_hyd)
    - 4.216 * np.log(Al2O3_Liq_mol_frac_hyd) + 63.3 * P2O5_Liq_mol_frac_hyd +
    1.264 * H2O_Liq_mol_frac_hyd + 2.457 * Al2O3_Amp_cat_23ox + 1.86 * K2O_Amp_cat_23ox
    + 0.4 * np.log(Na2O_Amp_cat_23ox / Na2O_Liq_mol_frac_hyd)))


def P_Put2016_eq7b(T=None, *, Al2O3_Liq_mol_frac_hyd, P2O5_Liq_mol_frac_hyd, Al2O3_Amp_cat_23ox,
    SiO2_Liq_mol_frac_hyd, Na2O_Liq_mol_frac_hyd, K2O_Liq_mol_frac_hyd, CaO_Liq_mol_frac_hyd):
    '''
    Amphibole-Liquid barometer: Equation 7b of Putirka et al. (2016)
    '''
    return (-64.79 - 6.064 * np.log(Al2O3_Amp_cat_23ox / Al2O3_Liq_mol_frac_hyd)
    + 61.75 * SiO2_Liq_mol_frac_hyd + 682 * P2O5_Liq_mol_frac_hyd
    - 101.9 *CaO_Liq_mol_frac_hyd + 7.85 * Al2O3_Amp_cat_23ox
    - 46.46 * np.log(SiO2_Liq_mol_frac_hyd)
    - 4.81 * np.log(Na2O_Liq_mol_frac_hyd + K2O_Liq_mol_frac_hyd))


def P_Put2016_eq7c(T=None, *, Al2O3_Amp_cat_23ox, K2O_Amp_cat_23ox,
                   P2O5_Liq_mol_frac, Al2O3_Liq_mol_frac, Na2O_Amp_cat_23ox, Na2O_Liq_mol_frac):
    '''
    Amphibole-Liquid barometer: Equation 7c of Putirka et al. (2016)
    '''
    return (-45.55 + 26.65 * Al2O3_Amp_cat_23ox + 22.52 * K2O_Amp_cat_23ox
    + 439 * P2O5_Liq_mol_frac - 51.1 * np.log(Al2O3_Liq_mol_frac) -
    46.3 * np.log(Al2O3_Amp_cat_23ox / (Al2O3_Liq_mol_frac))
    + 5.231 * np.log(Na2O_Amp_cat_23ox / (Na2O_Liq_mol_frac)))

## Equations: Amphibole-Liquid thermometers


def T_Put2016_eq4b(P=None, *, H2O_Liq_mol_frac_hyd, FeOt_Amp_cat_23ox, FeOt_Liq_mol_frac_hyd, MgO_Liq_mol_frac_hyd,
                   MnO_Liq_mol_frac_hyd, Al2O3_Liq_mol_frac_hyd, TiO2_Amp_cat_23ox, TiO2_Liq_mol_frac_hyd):
    '''
    Amphibole-Liquid thermometer: Eq4b,  Putirka et al. (2016)
    '''
    return (273.15 + (8037.85 / (3.69 - 2.62 * H2O_Liq_mol_frac_hyd + 0.66 * FeOt_Amp_cat_23ox
    - 0.416 * np.log(TiO2_Liq_mol_frac_hyd) + 0.37 * np.log(MgO_Liq_mol_frac_hyd)
    -1.05 * np.log((FeOt_Liq_mol_frac_hyd + MgO_Liq_mol_frac_hyd
    + MnO_Liq_mol_frac_hyd) * Al2O3_Liq_mol_frac_hyd)
    - 0.462 * np.log(TiO2_Amp_cat_23ox / TiO2_Liq_mol_frac_hyd))))


def T_Put2016_eq4a_amp_sat(P=None, *, FeOt_Liq_mol_frac_hyd, TiO2_Liq_mol_frac_hyd, Al2O3_Liq_mol_frac_hyd,
                           MnO_Liq_mol_frac_hyd, MgO_Liq_mol_frac_hyd, Na2O_Amp_cat_23ox, Na2O_Liq_mol_frac_hyd):
    '''
    Amphibole-Liquid thermometer Saturation surface of amphibole, Putirka et al. (2016)
    '''
    return (273.15 + (6383.4 / (-12.07 + 45.4 * Al2O3_Liq_mol_frac_hyd + 12.21 * FeOt_Liq_mol_frac_hyd -
    0.415 * np.log(TiO2_Liq_mol_frac_hyd) - 3.555 * np.log(Al2O3_Liq_mol_frac_hyd)
     - 0.832 * np.log(Na2O_Liq_mol_frac_hyd) -0.481 * np.log((FeOt_Liq_mol_frac_hyd
     + MgO_Liq_mol_frac_hyd + MnO_Liq_mol_frac_hyd) * Al2O3_Liq_mol_frac_hyd)
     - 0.679 * np.log(Na2O_Amp_cat_23ox / Na2O_Liq_mol_frac_hyd))))


def T_Put2016_eq9(P=None, *, SiO2_Amp_cat_23ox, TiO2_Amp_cat_23ox, MgO_Amp_cat_23ox,
FeOt_Amp_cat_23ox, Na2O_Amp_cat_23ox,  FeOt_Liq_mol_frac_hyd, Al2O3_Amp_cat_23ox, Al2O3_Liq_mol_frac_hyd,
K2O_Amp_cat_23ox, CaO_Amp_cat_23ox, Na2O_Liq_mol_frac_hyd, K2O_Liq_mol_frac_hyd):
    '''
    Amphibole-Liquid thermometer: Eq9,  Putirka et al. (2016)
    '''
    NaM4_1=2-FeOt_Amp_cat_23ox-CaO_Amp_cat_23ox
    NaM4=np.empty(len(NaM4_1))
    for i in range(0, len(NaM4)):
        if NaM4_1[i]<=0.1:
            NaM4[i]=0
        else:
            NaM4[i]=NaM4_1[i]

    HelzA=Na2O_Amp_cat_23ox-NaM4
    ln_KD_Na_K=np.log((K2O_Amp_cat_23ox/HelzA)*(Na2O_Liq_mol_frac_hyd/K2O_Liq_mol_frac_hyd))

    return (273.15+(10073.5/(9.75+0.934*SiO2_Amp_cat_23ox-1.454*TiO2_Amp_cat_23ox
    -0.882*MgO_Amp_cat_23ox-1.123*Na2O_Amp_cat_23ox-0.322*np.log(FeOt_Liq_mol_frac_hyd)
    -0.7593*np.log(Al2O3_Amp_cat_23ox/Al2O3_Liq_mol_frac_hyd)-0.15*ln_KD_Na_K)))



## Function: Amphibole-only temperature

Amp_only_T_funcs = {T_Put2016_eq5, T_Put2016_eq6, T_Put2016_SiHbl, T_Put2016_eq8,
 T_Ridolfi2012, T_Put2016_eq4a_amp_sat, T_Put2016_eq8} # put on outside

Amp_only_T_funcs_by_name= {p.__name__: p for p in Amp_only_T_funcs}




def calculate_amp_only_temp(amp_comps, equationT, P=None):
    '''
    Amphibole-only thermometry, calculates temperature in Kelvin.

    equationT: str
        |   T_Put2016_eq5 (P-independent)
        |   T_Put2016_eq6 (P-dependent)
        |   T_Put2016_SiHbl (P-independent)
        |   T_Ridolfi2012 (P-dependent)
        |   T_Put2016_eq8 (P-dependent)


    P: float, int, series, str  ("Solve")
        Pressure in kbar
        Only needed for P-sensitive thermometers.
        If enter P="Solve", returns a partial function
        Else, enter an integer, float, or panda series

    Returns
    -------
    pandas.series: Pressure in kbar (if eq_tests=False

    '''
    try:
        func = Amp_only_T_funcs_by_name[equationT]
    except KeyError:
        raise ValueError(f'{equationT} is not a valid equation') from None
    sig=inspect.signature(func)

    if sig.parameters['P'].default is not None:
        if P is None:
            raise ValueError(f'{equationT} requires you to enter P, or specify P="Solve"')
    else:
        if P is not None:
            print('Youve selected a P-independent function')

    if isinstance(P, pd.Series):
        if amp_comps is not None:
            if len(P) != len(amp_comps):
                raise ValueError('The panda series entered for Pressure isnt the same length as the dataframe of amphibole compositions')


    if equationT == "T_Ridolfi2012":
        if P is None:
            raise Exception(
                'You have selected a P-dependent thermometer, please enter an option for P')
        cat13 = calculate_13cations_amphibole_ridolfi(amp_comps)
        myAmps1_label = amp_comps.drop(['Sample_ID_Amp'], axis='columns')
        Sum_input = myAmps1_label.sum(axis='columns')

        kwargs = {name: cat13[name] for name, p in inspect.signature(
            T_Ridolfi2012).parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}

    else:
        amp_comps =calculate_23oxygens_amphibole(amp_comps=amp_comps)
        kwargs = {name: amp_comps[name] for name, p in sig.parameters.items()
        if p.kind == inspect.Parameter.KEYWORD_ONLY}


    if isinstance(P, str) or P is None:
        if P == "Solve":
            T_K = partial(func, **kwargs)
        if P is None:
            T_K=func(**kwargs)

    else:
        T_K=func(P, **kwargs)

    return T_K


## Function: PT Iterate Amphibole - only

def calculate_amp_only_press_temp(amp_comps, equationT, equationP, iterations=30, T_K_guess=1300):
    '''
    Solves simultaneous equations for temperature and pressure using
    amphibole only thermometers and barometers.


   Parameters
    -------

    amp_comps: DataFrame
        Amphibole compositions with column headings SiO2_Amp, MgO_Amp etc.

    EquationP: str

        | P_Mutch2016 (T-independent)
        | P_Ridolfi2012_1a (T-independent)
        | P_Ridolfi2012_1b (T-independent)
        | P_Ridolfi2012_1c (T-independent)
        | P_Ridolfi2012_1d (T-independent)
        | P_Ridolfi2012_1e (T-independent)
        | P_Ridolfi2021 - (T-independent)- Uses new algorithm in 2021 paper to
        select pressures from equations 1a-e.

        | P_Ridolfi2010  (T-independent)
        | P_Hammerstrom1986_eq1  (T-independent)
        | P_Hammerstrom1986_eq2 (T-independent)
        | P_Hammerstrom1986_eq3 (T-independent)
        | P_Hollister1987 (T-independent)
        | P_Johnson1989 (T-independent)
        | P_Blundy1990 (T-independent)
        | P_Schmidt1992 (T-independent)
        | P_Anderson1995 (*T-dependent*)

    equationT: str
        |   T_Put2016_eq5 (P-independent)
        |   T_Put2016_eq6 (P-dependent)
        |   T_Put2016_SiHbl (P-independent)
        |   T_Ridolfi2012 (P-dependent)
        |   T_Put2016_eq8 (P-dependent)

    H2O_Liq: float, int, series, optional
        Needed if you select P_Put2008_eq32b, which is H2O-dependent.

    Optional:

     iterations: int, default=30
         Number of iterations used to converge to solution.

     T_K_guess: int or float. Default is 1300 K
         Initial guess of temperature.


    Returns:
    -------
    panda.dataframe: Pressure in Kbar, Temperature in K
    '''
    T_func = calculate_amp_only_temp(amp_comps=amp_comps, equationT=equationT, P="Solve")
    if equationP !="P_Ridolfi2021" and equationP != "P_Mutch2016":
        P_func = calculate_amp_only_press(amp_comps=amp_comps, equationP=equationP, T="Solve")
    else:
        P_func = calculate_amp_only_press(amp_comps=amp_comps, equationP=equationP, T="Solve").P_kbar_calc
    if isinstance(T_func, pd.Series) and isinstance(P_func, pd.Series):
        P_guess = P_func
        T_K_guess = T_func

    if isinstance(T_func, pd.Series) and isinstance(P_func, partial):
        P_guess = P_func(T_func)
        T_K_guess = T_func

    if isinstance(P_func, pd.Series) and isinstance(T_func, partial):
        T_K_guess = T_func(P_func)
        P_guess = P_func

    if isinstance(P_func, partial) and isinstance(T_func, partial):

        for _ in range(iterations):
            P_guess = P_func(T_K_guess)
            T_K_guess = T_func(P_guess)


    PT_out = pd.DataFrame(data={'P_kbar_calc': P_guess, 'T_K_calc': T_K_guess})
    return PT_out

## Function: Amphibole-Liquid barometer
Amp_Liq_P_funcs = {P_Put2016_eq7a, P_Put2016_eq7b, P_Put2016_eq7c}

Amp_Liq_P_funcs_by_name = {p.__name__: p for p in Amp_Liq_P_funcs}


def calculate_amp_liq_press(*, amp_comps=None, liq_comps=None,
                            meltmatch=None, equationP=None, T=None,
                             eq_tests=False, H2O_Liq=None):
    '''
    Amphibole-liquid barometer. Returns pressure in kbar

   Parameters
    -------

    amp_comps: pandas DataFrame
        amphibole compositions (SiO2_Amp, TiO2_Amp etc.)

    liq_comps: pandas DataFrame
        liquid compositions (SiO2_Liq, TiO2_Liq etc.)

    equationP: str
        | P_Put2016_eq7a (T-independent, H2O-dependent)
        | P_Put2016_eq7b (T-independent, H2O-dependent (as hyd frac))
        | P_Put2016_eq7c (T-independent, H2O-dependent (as hyd frac))

    P: float, int, series, str  ("Solve")
        Pressure in kbar
        Only needed for P-sensitive thermometers.
        If enter P="Solve", returns a partial function
        Else, enter an integer, float, or panda series


    Eq_Test: bool. Default False
        If True, also calcualtes Kd Fe-Mg, which Putirka (2016) suggest
        as an equilibrium test.


    Returns
    -------
    pandas.core.series.Series (for simple barometers)
        Pressure in kbar
    pandas DataFrame for barometers like P_Ridolfi_2021, P_Mutch2016

    '''
    try:
        func = Amp_Liq_P_funcs_by_name[equationP]
    except KeyError:
        raise ValueError(f'{equationP} is not a valid equation') from None
    sig=inspect.signature(func)

    if sig.parameters['T'].default is not None:
        if T is None:
            raise ValueError(f'{equationP} requires you to enter T, or specify T="Solve"')
    else:
        if T is not None:
            print('Youve selected a T-independent function')

    if isinstance(T, pd.Series):
        if liq_comps is not None:
            if len(T) != len(liq_comps):
                raise ValueError('The panda series entered for Temperature isnt the same length as the dataframe of liquid compositions')


    if meltmatch is not None:
        Combo_liq_amps = meltmatch
    if liq_comps is not None and amp_comps is not None:
        liq_comps_c = liq_comps.copy()
        if H2O_Liq is not None:
            liq_comps_c['H2O_Liq'] = H2O_Liq

        amp_comps_23 = calculate_23oxygens_amphibole(amp_comps=amp_comps)
        liq_comps_hy = calculate_hydrous_cat_fractions_liquid(
            liq_comps=liq_comps_c)
        liq_comps_an = calculate_anhydrous_cat_fractions_liquid(
            liq_comps=liq_comps_c)
        Combo_liq_amps = pd.concat(
            [amp_comps_23, liq_comps_hy, liq_comps_an], axis=1)


    kwargs = {name: Combo_liq_amps[name] for name, p in sig.parameters.items() if p.kind == inspect.Parameter.KEYWORD_ONLY}
    if isinstance(T, str) or T is None:
        if T == "Solve":
            P_kbar = partial(func, **kwargs)
        if T is None:
            P_kbar=func(**kwargs)

    else:
        P_kbar=func(T, **kwargs)

    if eq_tests is False:
        return P_kbar
    if eq_tests is True:
        MolProp=calculate_mol_proportions_amphibole(amp_comps=amp_comps)
        Kd=(MolProp['FeOt_Amp_mol_prop']/MolProp['MgO_Amp_mol_prop'])/(liq_comps_hy['FeOt_Liq_mol_frac_hyd']/liq_comps_hy['MgO_Liq_mol_frac_hyd'])

        b = np.empty(len(MolProp), dtype=str)
        for i in range(0, len(MolProp)):

            if Kd[i] >= 0.17 and Kd[i] <= 0.39:
                b[i] = str("Yes")
            else:
                b[i] = str("No")
        Out=pd.DataFrame(data={'P_kbar_calc': P_kbar, 'Kd-Fe-Mg': Kd, "Eq Putirka 2016?": b})
    return Out
## Function: Amp-Liq temp

Amp_Liq_T_funcs = {T_Put2016_eq4b,  T_Put2016_eq4a_amp_sat, T_Put2016_eq9}

Amp_Liq_T_funcs_by_name = {p.__name__: p for p in Amp_Liq_T_funcs}

def calculate_amp_liq_temp(*, amp_comps=None, liq_comps=None, equationT=None,
P=None, H2O_Liq=None, eq_tests=False):
    '''
    Amphibole-liquid thermometers. Returns temperature in Kelvin.

   Parameters
    -------
    amp_comps: pandas DataFrame
        amphibole compositions (SiO2_Amp, TiO2_Amp etc.)

    liq_comps: pandas DataFrame
        liquid compositions (SiO2_Liq, TiO2_Liq etc.)

    equationT: str
        T_Put2016_eq4a_amp_sat (P-independent, H2O-dep through hydrous fractions)
        T_Put2016_eq4b (P-independent, H2O-dep)
        T_Put2016_eq9 (P-independent, H2O-dep through hydrous fractions)

    P: float, int, series, str  ("Solve")
        Pressure in kbar
        Only needed for P-sensitive thermometers.
        If enter P="Solve", returns a partial function
        Else, enter an integer, float, or panda series

    Eq_Test: bool. Default False
        If True, also calcualtes Kd Fe-Mg, which Putirka (2016) suggest
        as an equilibrium test.


    Returns
    -------
    pandas.core.series.Series
        Temperature in Kelvin
    '''
    try:
        func = Amp_Liq_T_funcs_by_name[equationT]
    except KeyError:
        raise ValueError(f'{equationT} is not a valid equation') from None
    sig=inspect.signature(func)

    if sig.parameters['P'].default is not None:
        if P is None:
            raise ValueError(f'{equationT} requires you to enter P, or specify P="Solve"')
    else:
        if P is not None:
            print('Youve selected a P-independent function')

    if isinstance(P, pd.Series):
        if liq_comps is not None:
            if len(P) != len(liq_comps):
                raise ValueError('The panda series entered for Pressure isnt the same length as the dataframe of liquid compositions')


    if liq_comps is not None:
        liq_comps_c = liq_comps.copy()
        if H2O_Liq is not None:
            liq_comps_c['H2O_Liq'] = H2O_Liq

    amp_comps_23 = calculate_23oxygens_amphibole(amp_comps=amp_comps)
    liq_comps_hy = calculate_hydrous_cat_fractions_liquid(liq_comps=liq_comps_c)
    liq_comps_an = calculate_anhydrous_cat_fractions_liquid(liq_comps=liq_comps_c)
    Combo_liq_amps = pd.concat([amp_comps_23, liq_comps_hy, liq_comps_an], axis=1)
    kwargs = {name: Combo_liq_amps[name] for name, p in sig.parameters.items()
    if p.kind == inspect.Parameter.KEYWORD_ONLY}


    if isinstance(P, str) or P is None:
        if P == "Solve":
            T_K = partial(func, **kwargs)
        if P is None:
            T_K=func(**kwargs)

    else:
        T_K=func(P, **kwargs)


    if eq_tests is False:
        return T_K
    if eq_tests is True:
        MolProp=calculate_mol_proportions_amphibole(amp_comps=amp_comps)
        Kd=((MolProp['FeOt_Amp_mol_prop']/MolProp['MgO_Amp_mol_prop'])/
        (liq_comps_hy['FeOt_Liq_mol_frac_hyd']/liq_comps_hy['MgO_Liq_mol_frac_hyd']))

        b = np.empty(len(MolProp), dtype=str)
        for i in range(0, len(MolProp)):

            if Kd[i] >= 0.17 and Kd[i] <= 0.39:
                b[i] = str("Yes")
            else:
                b[i] = str("No")
        Out=pd.DataFrame(data={'T_K_calc': T_K, 'Kd-Fe-Mg': Kd, "Eq Putirka 2016?": b})
    return Out

## Function for amphibole-liquid PT iter (although technically not needed)


def calculate_amp_liq_press_temp(liq_comps, amp_comps, equationT, equationP, iterations=30,
T_K_guess=1300, H2O_Liq=None, eq_tests=False):
    '''
    Solves simultaneous equations for temperature and pressure using
    amphibole only thermometers and barometers.


   Parameters
    -------

    amp_comps: DataFrame
        Amphibole compositions with column headings SiO2_Amp, MgO_Amp etc.

    equationP: str
        | P_Put2016_eq7a (T-independent, H2O-dependent (as hyd frac))
        | P_Put2016_eq7b (T-independent, H2O-dependent (as hyd frac))
        | P_Put2016_eq7c (T-independent, H2O-dependent (as hyd frac))

    equationT: str
        T_Put2016_eq4a_amp_sat (P-independent, H2O-dep through hydrous fractions)
        T_Put2016_eq4b (P-independent, H2O-dep through hydrous fractions)
        T_Put2016_eq9 (P-independent, H2O-dep through hydrous fractions)


    H2O_Liq: float, int, series, optional
        Needed if you select P_Put2008_eq32b, which is H2O-dependent.

    Optional:

    iterations: int, default=30
         Number of iterations used to converge to solution.

    T_K_guess: int or float. Default is 1300 K
         Initial guess of temperature.

    Eq_Test: bool. Default False
        If True, also calcualtes Kd Fe-Mg, which Putirka (2016) suggest
        as an equilibrium test.



    Returns:
    -------
    panda.dataframe: Pressure in Kbar, Temperature in K, Kd-Fe-Mg if Eq_Test=True
    '''
    liq_comps_c=liq_comps.copy()
    if H2O_Liq is not None:
        liq_comps_c['H2O_Liq']=H2O_Liq

    T_func = calculate_amp_liq_temp(liq_comps=liq_comps_c,
    amp_comps=amp_comps, equationT=equationT, P="Solve")

    P_func = calculate_amp_liq_press(liq_comps=liq_comps_c,
    amp_comps=amp_comps, equationP=equationP, T="Solve")

    if isinstance(T_func, pd.Series) and isinstance(P_func, pd.Series):
        P_guess = P_func
        T_K_guess = T_func

    if isinstance(T_func, pd.Series) and isinstance(P_func, partial):
        P_guess = P_func(T_func)
        T_K_guess = T_func

    if isinstance(P_func, pd.Series) and isinstance(T_func, partial):
        T_K_guess = T_func(P_func)
        P_guess = P_func

    if isinstance(P_func, partial) and isinstance(T_func, partial):

        for _ in range(iterations):
            P_guess = P_func(T_K_guess)
            T_K_guess = T_func(P_guess)


    PT_out = pd.DataFrame(data={'P_kbar_calc': P_guess, 'T_K_calc': T_K_guess})

    if eq_tests is False:
        return PT_out
    if eq_tests is True:
        liq_comps_hy = calculate_hydrous_cat_fractions_liquid(
            liq_comps=liq_comps_c)
        MolProp=calculate_mol_proportions_amphibole(amp_comps=amp_comps)
        Kd=(MolProp['FeOt_Amp_mol_prop']/MolProp['MgO_Amp_mol_prop'])/(liq_comps_hy['FeOt_Liq_mol_frac_hyd']/liq_comps_hy['MgO_Liq_mol_frac_hyd'])
        PT_out['Kd-Fe-Mg']=Kd

        b = np.empty(len(MolProp), dtype=str)
        for i in range(0, len(MolProp)):

            if Kd[i] >= 0.17 and Kd[i] <= 0.39:
                b[i] = str("Yes")
            else:
                b[i] = str("No")

        PT_out["Eq Putirka 2016?"]=b

    return PT_out
