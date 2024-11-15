from rdkit import Chem
from rdkit.Chem import Draw

# Создаем молекулы
methane = Chem.MolFromSmiles("C")
penten = Chem.MolFromSmiles("CC=CCC")  # Исправленный SMILES для пентена
phenylalanine = Chem.MolFromSmiles("C1=CC=C(C=C1)CC(C(=O)O)N")  # Фенилаланин
phenylalanine_iso = Chem.MolFromSmiles("C1=CC=C(C=C1)CC(C(=O)O)N")  # Изомер фенилаланина (такой же SMILES)

# Количество атомов в фенилаланине
if phenylalanine:
    num_phenylalanine = phenylalanine.GetNumAtoms()
    print(f"Количество атомов в молекуле фенилаланина: {num_phenylalanine}")
else:
    print("Ошибка: не удалось создать молекулу фенилаланина.")

# Учет водородов с использованием AddHs
if phenylalanine:
    phenylalanine_h = Chem.AddHs(phenylalanine)
    num_phenylalanine_h = phenylalanine_h.GetNumAtoms()
    print(f"Количество атомов в фенилаланине (включая водороды): {num_phenylalanine_h}")
else:
    print("Ошибка: не удалось создать молекулу фенилаланина с учетом водородов.")

# Создаем молекулу с дополнительными свойствами атомов
mol = Chem.MolFromSmiles('c1ccccc(C(N)=O)1')  # Молекула с аминогруппой на бензольном кольце
if mol:
    # Добавляем номера атомов
    for i, atom in enumerate(mol.GetAtoms()):
        atom.SetProp("molAtomMapNumber", str(atom.GetIdx() + 1))
    Draw.MolToImage(mol).show()

    # Добавляем пользовательские метки
    for i, atom in enumerate(mol.GetAtoms()):
        atom.SetProp("atomLabel", f"a{i+1}")
    Draw.MolToImage(mol).show()

    # Отмечаем атомы азота
    for atom in mol.GetAtoms():
        if atom.GetSymbol() == "N":
            atom.SetProp("atomNote", "Nitrogen")
    Draw.MolToImage(mol).show()
else:
    print("Ошибка: не удалось создать молекулу для отображения.")
