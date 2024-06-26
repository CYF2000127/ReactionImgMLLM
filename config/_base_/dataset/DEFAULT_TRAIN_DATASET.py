_base_ = [
    # 'DEFAULT_TRAIN_GQA_VARIANT.py',
    # 'DEFAULT_TRAIN_CLEVR_VARIANT.py',
    # 'DEFAULT_TRAIN_POINT_VARIANT.py',
    # 'DEFAULT_TRAIN_GPTGEN_VARIANT.py',
    # 'DEFAULT_TRAIN_VCR_VARIANT.py',
    # 'DEFAULT_TRAIN_VQAv2_VARIANT.py',
    # 'DEFAULT_TRAIN_VQAEX_VARIANT.py',
]

DEFAULT_TRAIN_DATASET = dict(
    flickr=dict(
        type='FlickrDataset',
        filename=r'./reactiondata/reaction_train.jsonl',
        image_folder=r'./reaction_image',
        template_file=r'./config/_base_/dataset/template/reaction.json',
    )
    # rec=dict(
    #     type='RECDataset',
    #     filename=r'{{fileDirname}}/../../../data/REC_ref3_train.jsonl',
    #     image_folder=r'zz1424:s3://visual_grounding/academic_data/refer/images/mscoco/images/train2014/',
    #     template_file=r'{{fileDirname}}/template/REC.json',
    # ),
    # recvg=dict(
    #     type='RECDataset',
    #     filename=r'{{fileDirname}}/../../../data/GC_genome196_train.jsonl',
    #     image_folder=r'zz1424:s3://publicdataset_8/Visual_Genome_Dataset_V1.2/unzip/data',
    #     template_file=r'{{fileDirname}}/template/REC.json',
    # ),
    # reg=dict(
    #     type='REGDataset',
    #     filename=r'{{fileDirname}}/../../../data/REC_ref3_train.jsonl',
    #     image_folder=r'zz1424:s3://visual_grounding/academic_data/refer/images/mscoco/images/train2014/',
    #     template_file=r'{{fileDirname}}/template/REG.json',
    # ),
    # gc=dict(
    #     type='GCDataset',
    #     filename=r'{{fileDirname}}/../../../data/GC_genome196_train.jsonl',
    #     image_folder=r'zz1424:s3://publicdataset_8/Visual_Genome_Dataset_V1.2/unzip/data',
    #     template_file=r'{{fileDirname}}/template/GC.json',
    # ),
    # caption=dict(
    #     type='CaptionDataset',
    #     filename=r'{{fileDirname}}/../../../data/CAP_coco2014_train.jsonl',
    #     image_folder=r'openmmlab1424:s3://openmmlab/datasets/detection/coco/train2014/',
    #     template_file=r'{{fileDirname}}/template/image_cap.json',
    # ),
    # llavacc3m=dict(
    #     type='InstructDataset',
    #     filename=r"{{fileDirname}}/../../../data/llava_cc3m.jsonl",
    #     image_folder=r'sh41:s3://MultiModal/Monolith/academic/llava-pretrain/data/558K_imgs',  # TODO: zz make folder name mistake
    # ),
    # llavalcs=dict(
    #     type='InstructDataset',
    #     filename=r"{{fileDirname}}/../../../data/blip_laion_cc_sbu_558k.jsonl",
    #     image_folder=r'sh41:s3://MultiModal/Monolith/academic/llava-pretrain/data/595K_imgs',  # TODO: zz make folder name mistake
    # ),
    # instruct=dict(
    #     type='InstructDataset',
    #     filename=r'{{fileDirname}}/../../../data/llava_instruct_150k.jsonl',
    #     image_folder=r'zz1424:s3://PublicDatalist/public_datalist_6_unzip/train2014',
    #     add_coco_prefix=True,
    #),
    # **_base_.DEFAULT_TRAIN_GQA_VARIANT,
    # **_base_.DEFAULT_TRAIN_CLEVR_VARIANT,
    # **_base_.DEFAULT_TRAIN_POINT_VARIANT,
    # **_base_.DEFAULT_TRAIN_GPTGEN_VARIANT,
    # **_base_.DEFAULT_TRAIN_VCR_VARIANT,
    # **_base_.DEFAULT_TRAIN_VQAv2_VARIANT,
    # **_base_.DEFAULT_TRAIN_VQAEX_VARIANT,
)
