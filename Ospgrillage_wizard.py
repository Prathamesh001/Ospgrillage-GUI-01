import tkinter as tk
from tkinter import ttk
import make_material

def create_label_entry(frame, text, row):
    label = ttk.Label(frame, text=text)
    label.grid(row=row, column=0, padx=5, pady=2, sticky='w')
    entry = ttk.Entry(frame)
    entry.grid(row=row, column=1, padx=5, pady=2)
    return entry

def solve():
    values = {"Model Name": model_name_entry.get(), "E": e_entry.get(), "G": g_entry.get(), "ν": v_entry.get(), "ρ": p_entry.get(),
              "A": a_entry.get(), "J": j_entry.get(), "Iz": iz_entry.get(), "Iy": iy_entry.get(),
              "Az": az_entry.get(), "Ay": ay_entry.get(), "L": l_entry.get(), "W": w_entry.get(),
              "n-l": nl_entry.get(), "n-t": nt_entry.get(), "Skew Angle": skew_angle_entry.get(), "Mesh Type": mesh_type_entry.get(),
              "Nodal Load": node_load_entry.get(), "Patch Load": patch_load_entry.get()}
    #create material
    E, G, v, p = e_entry.get(), g_entry.get(), v_entry.get(), p_entry.get() 
    material = make_material.create_the_material(E,G,v,p)
    #create section
    A, J, Iy, Iz, Ay, Az = a_entry.get(), j_entry.get(), iy_entry.get(), iz_entry.get(), ay_entry.get(), az_entry.get()
    section = make_material.section(A, J, Iy, Iz, Ay, Az)
    #create model
    model_name, skew_angle, mesh_type, L, w, n_l, n_t = model_name_entry.get(), skew_angle_entry.get(), mesh_type_entry.get(), l_entry.get(), w_entry.get(), nl_entry.get(), nt_entry.get()
    model = make_material.make_model(model_name, skew_angle, mesh_type, L, w, n_l, n_t, material, section)
    #Plot model
    make_material.plot_model(model)
    #print(A, J, Iy, Iz, Ay, Az)
    #print(section)
    #print(material)
    #print(E, G, v, p)

def create_gui():
    global model_name_entry, e_entry, g_entry, v_entry, p_entry, a_entry, j_entry, iz_entry, iy_entry, az_entry, ay_entry
    global l_entry, w_entry, nl_entry, nt_entry, skew_angle_entry, mesh_type_entry, node_load_entry, patch_load_entry
    
    root = tk.Tk()
    root.title("Ospgrillage GUI")
    
    # Model Name Frame
    model_frame = ttk.LabelFrame(root, text="Model Information")
    model_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')
    model_name_entry = create_label_entry(model_frame, "Model Name", 0)
    
    # Material Properties Frame
    material_frame = ttk.LabelFrame(root, text="Material Properties")
    material_frame.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')
    
    e_entry = create_label_entry(material_frame, "E (Young's Mod.)", 0)
    g_entry = create_label_entry(material_frame, "G (Shear Mod.)", 1)
    v_entry = create_label_entry(material_frame, "ν (Poisson's Ratio)", 2)
    p_entry = create_label_entry(material_frame, "ρ (Density)", 3)
    
    # Cross Section Properties Frame
    section_frame = ttk.LabelFrame(root, text="Cross Section Properties")
    section_frame.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')
    
    a_entry = create_label_entry(section_frame, "A (C/S Area)", 0)
    j_entry = create_label_entry(section_frame, "J (MOI Qx)", 1)
    iz_entry = create_label_entry(section_frame, "Iz (MOI Z)", 2)
    iy_entry = create_label_entry(section_frame, "Iy (MOI Y)", 3)
    az_entry = create_label_entry(section_frame, "Az (C/S Aintz)", 4)
    ay_entry = create_label_entry(section_frame, "Ay (C/S Ainty)", 5)
    
    # Grillage Model Frame
    grillage_frame = ttk.LabelFrame(root, text="Grillage Model")
    grillage_frame.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')
    
    l_entry = create_label_entry(grillage_frame, "L (Length)", 0)
    w_entry = create_label_entry(grillage_frame, "W (Width)", 1)
    nl_entry = create_label_entry(grillage_frame, "n-l (Long Grid Lines)", 2)
    nt_entry = create_label_entry(grillage_frame, "n-t (Transverse Members)", 3)
    skew_angle_entry = create_label_entry(grillage_frame, "Skew Angle", 4)
    mesh_type_entry = create_label_entry(grillage_frame, "Mesh Type (Oblique/Ortho)", 5)
    
    # Loading Frame
    loading_frame = ttk.LabelFrame(root, text="Loading")
    loading_frame.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')
    
    node_load_entry = create_label_entry(loading_frame, "Nodal Load", 0)
    patch_load_entry = create_label_entry(loading_frame, "Patch Load", 1)
    
    # Button
    print_button = ttk.Button(root, text="Solve", command=solve)
    print_button.grid(row=3, column=1, padx=10, pady=10, sticky='se')
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()


