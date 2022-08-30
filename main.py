from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_FACE
from OCC.Core.StepRepr import StepRepr_RepresentationItem

reader = STEPControl_Reader()
tr = reader.WS().TransferReader()
reader.ReadFile('model.stp')
reader.TransferRoots()
model = reader.StepModel()
shape = reader.OneShape()


exp = TopExp_Explorer(shape, TopAbs_FACE)
while exp.More():
    s = exp.Current()
    exp.Next()

    item = tr.EntityFromShapeResult(s, 1)
    item = StepRepr_RepresentationItem.DownCast(item)

    label = item.Name().ToCString()
    id = model.IdentLabel(item)

    print('label', label)
    print('id', id)
