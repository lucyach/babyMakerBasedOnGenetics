import random
# Class Gene holds all the genes we will apply to Person
class Genotype:
  def __init__(self, name, allelle1, allelle2):
    self.name = name
    self.allelle1 = allelle1
    self.allelle2 = allelle2
  
  def getChildAllelle(self):
    allelle = random.randint(1, 2)
    if allelle == 1:
      return self.allelle1
    else:
      return self.allelle2

# Defines a person
class Person:
  def __init__(self, name, genes):
    self.name = name
    self.genes = genes
  
  def makeChild(self, parent2, name):
    childsGenes = {}
    for gene in self.genes.values():
      genotype = Genotype(gene.name, gene.getChildAllelle(), parent2.genes[gene.name].getChildAllelle())
      childsGenes[gene.name] = genotype
    return Person(name, childsGenes)
  
  def __str__(self):
    personstr = "Name: " + self.name + "\n"
    for gene in self.genes.values():
      together_genotype = gene.allelle1 + gene.allelle2
      phenotype = "N/A"
      # eye color
      if gene.name == "eyecolor":
        if together_genotype == "BB" or together_genotype == "Bb" or together_genotype == "bB":
          phenotype = "brown eyes"
        else:
          phenotype = "blue eyes"
      # height
      if gene.name == "height":
        if together_genotype == "TT":
          phenotype = "tall"
        elif together_genotype == "Tt" or together_genotype == "tT":
          phenotype = "average"
        else:
          phenotype = "short"
      # hair color
      if gene.name == "haircolor":
        if together_genotype == "BB" or together_genotype == "Bb" or together_genotype == "bB":
          phenotype = "brown hair"
        else:
          phenotype = "blond hair"
      personstr += gene.name + ": " + together_genotype + " (" + phenotype + ")" + "\n"
      
    return personstr


# Make a person
# eye color, height, hair color
mom1 = Person("mom1", {"eyecolor" : Genotype("eyecolor", "B", "b"), "height" : Genotype("height", "T", "t"), "haircolor" : Genotype("haircolor", "B", "b")})
dad1 = Person("dad1", {"eyecolor" : Genotype("eyecolor", "b", "b"), "height" : Genotype("height", "T", "t"), "haircolor" : Genotype("haircolor", "B", "b")})
mom2 = Person("mom2", {"eyecolor" : Genotype("eyecolor", "B", "b"), "height" : Genotype("height", "t", "t"), "haircolor" : Genotype("haircolor", "B", "b")})
dad2 = Person("dad2", {"eyecolor" : Genotype("eyecolor", "B", "b"), "height" : Genotype("height", "T", "t"), "haircolor" : Genotype("haircolor", "B", "b")})


baby1 = mom1.makeChild(dad1, "child1")
baby2 = mom2.makeChild(dad2, "child2")
baby3 = baby1.makeChild(baby2, "child3")
print mom1
print dad1
print baby1
print mom2
print dad2
print baby2
print baby3

valueCounts = {"BB" : 0, "Bb" : 0, "bB" : 0, "bb" : 0}

for i in range(0, 100):
  baby4 = mom2.makeChild(dad2, "child4")
  baby4_genotype = baby4.genes["eyecolor"].allelle1 + baby4.genes["eyecolor"].allelle2
  valueCounts[baby4_genotype] += 1
print valueCounts

# Don't worry about how this works because it doesn't work
averageValueCounts = {"BB" : 0, "Bb" : 0, "bB" : 0, "bb" : 0}
valueCounts = {"BB" : 0, "Bb" : 0, "bB" : 0, "bb" : 0}
for i in range(100):
  for i in range(100):
    baby4 = mom2.makeChild(dad2, "child4")
    baby4_genotype = baby4.genes["eyecolor"].allelle1 + baby4.genes["eyecolor"].allelle2
    valueCounts[baby4_genotype] += 1
  for genotype in ["BB", "Bb", "bB", "bb"]:
    averageValueCounts[genotype] += valueCounts[genotype]
  
  
print averageValueCounts










