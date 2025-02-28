import ospgrillage as og
#This module creates the material for the model
def create_the_material(E, G, v, p): #Youngs modulus, Shear modulus, Poisson's ratio, Density
    mtrial = og.create_material(E=float(E), G =float(G), v= float(v), rho=float(p))
    print("Material created")
    return mtrial

def section(A, J, Iy, Iz, Ay, Az):
    created_section = og.create_section(
    A=float(A),
    J=float(J),
    Iy=float(Iy),
    Iz=float(Iz),
    Ay=float(Ay),
    Az=float(Az),
    )
    print("1")
    
    print("2")
    return created_section
def make_model(model_name, skew_angle, mesh_type, L, w, n_l, n_t, material, created_section):
    print(created_section)
    print(material)
    model = og.create_grillage(
        bridge_name=str(model_name),
        long_dim=float(L),
        width=float(w),
        skew=float(skew_angle),
        mesh_type = str(mesh_type),
        num_long_grid=int(n_l),
        #beam_z_spacing = [1, 5, 10, 11.565],
        num_trans_grid=int(n_t),
        #beam_x_spacing = [1, 3, 8, 9],
        #edge_beam_dist=edge_dist,
        #ext_to_int_dist = ext_to_int_dist,
    )
    # assign grillage member to element groups of grillage model
    print("3")
    beam = og.create_member(section=created_section, material=material)
    model.set_member(beam, member="interior_main_beam")
    model.set_member(beam, member="exterior_main_beam_1")
    model.set_member(beam, member="exterior_main_beam_2")
    model.set_member(beam, member="edge_beam")
    model.set_member(beam, member="transverse_slab")
    model.set_member(beam, member="start_edge")
    model.set_member(beam, member="end_edge")
    print("4")
    return model
def plot_model(model):
    model.create_osp_model(pyfile=False)
    og.opsplt.plot_model(show_nodes="yes",show_nodetags="yes",);
    og.opsv.plot_model(az_el=(-90, 0),element_labels=0);
    fig = og.plt.gcf()
    fig.set_size_inches(8, 8)
    og.plt.show()
