def convert_to_yolov8(label_file_path, image_sizes):
    with open(label_file_path, 'r') as file:
        lines = file.readlines()

    yolo_labels = []
    current_image_size = None

    for line in lines:
        line = line.strip()

        # Check if line contains image size information
        if line.endswith('.jpg:'):
            current_image_size = image_sizes[line[:-5]]
            continue

        # Split line into parts
        parts = line.split()

        # Skip lines with less than 6 elements
        if len(parts) < 6:
            continue

        # Extract relevant information
        class_id = int(parts[0])
        x, y, w, h = map(float, parts[1:5])

        # Convert bounding box coordinates to percentages
        x /= current_image_size[0]
        y /= current_image_size[1]
        w /= current_image_size[0]
        h /= current_image_size[1]

        # Calculate center coordinates
        x_center = x + w / 2
        y_center = y + h / 2

        # Create YOLOv8 label string
        yolo_label = f"{class_id} {x_center} {y_center} {w} {h}"

        yolo_labels.append(yolo_label)

    return yolo_labels


label_file_path = 'Data\\29--Students_Schoolkids.txt'  # Replace with your actual file path
image_sizes = {
    '29_Students_Schoolkids_Students_Schoolkids_29_102.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_108.jpg': (1024, 621),
'29_Students_Schoolkids_Students_Schoolkids_29_110.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_112.jpg': (1024, 787),
'29_Students_Schoolkids_Students_Schoolkids_29_114.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_119.jpg': (1024, 671),
'29_Students_Schoolkids_Students_Schoolkids_29_123.jpg': (1024, 1434),
'29_Students_Schoolkids_Students_Schoolkids_29_127.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_131.jpg': (1024, 579),
'29_Students_Schoolkids_Students_Schoolkids_29_137.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_141.jpg': (1024, 579),
'29_Students_Schoolkids_Students_Schoolkids_29_160.jpg': (1024, 469),
'29_Students_Schoolkids_Students_Schoolkids_29_165.jpg': (1024, 682),
'29_Students_Schoolkids_Students_Schoolkids_29_175.jpg': (1024, 1296),
'29_Students_Schoolkids_Students_Schoolkids_29_179.jpg': (1024, 663),
'29_Students_Schoolkids_Students_Schoolkids_29_18.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_181.jpg': (1024, 662),
'29_Students_Schoolkids_Students_Schoolkids_29_184.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_186.jpg': (1024, 733),
'29_Students_Schoolkids_Students_Schoolkids_29_187.jpg': (1024, 1536),
'29_Students_Schoolkids_Students_Schoolkids_29_19.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_190.jpg': (1024, 871),
'29_Students_Schoolkids_Students_Schoolkids_29_2.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_215.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_220.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_224.jpg': (1024, 730),
'29_Students_Schoolkids_Students_Schoolkids_29_227.jpg': (1024, 687),
'29_Students_Schoolkids_Students_Schoolkids_29_228.jpg': (1024, 615),
'29_Students_Schoolkids_Students_Schoolkids_29_230.jpg': (1024, 522),
'29_Students_Schoolkids_Students_Schoolkids_29_231.jpg': (1024, 702),
'29_Students_Schoolkids_Students_Schoolkids_29_24.jpg': (1024, 1024),
'29_Students_Schoolkids_Students_Schoolkids_29_258.jpg': (1024, 716),
'29_Students_Schoolkids_Students_Schoolkids_29_259.jpg': (1024, 1583),
'29_Students_Schoolkids_Students_Schoolkids_29_261.jpg': (1024, 1547),
'29_Students_Schoolkids_Students_Schoolkids_29_262.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_267.jpg': (1024, 664),
'29_Students_Schoolkids_Students_Schoolkids_29_268.jpg': (1024, 1024),
'29_Students_Schoolkids_Students_Schoolkids_29_269.jpg': (1024, 579),
'29_Students_Schoolkids_Students_Schoolkids_29_27.jpg': (1024, 1095),
'29_Students_Schoolkids_Students_Schoolkids_29_274.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_275.jpg': (1024, 680),
'29_Students_Schoolkids_Students_Schoolkids_29_276.jpg': (1024, 551),
'29_Students_Schoolkids_Students_Schoolkids_29_278.jpg': (1024, 815),
'29_Students_Schoolkids_Students_Schoolkids_29_281.jpg': (1024, 820),
'29_Students_Schoolkids_Students_Schoolkids_29_282.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_287.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_288.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_293.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_298.jpg': (1024, 558),
'29_Students_Schoolkids_Students_Schoolkids_29_30.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_300.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_305.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_309.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_313.jpg': (1024, 700),
'29_Students_Schoolkids_Students_Schoolkids_29_315.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_324.jpg': (1024, 769),
'29_Students_Schoolkids_Students_Schoolkids_29_325.jpg': (1024, 1024),
'29_Students_Schoolkids_Students_Schoolkids_29_327.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_33.jpg': (1024, 712),
'29_Students_Schoolkids_Students_Schoolkids_29_334.jpg': (1024, 679),
'29_Students_Schoolkids_Students_Schoolkids_29_335.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_336.jpg': (1024, 1396),
'29_Students_Schoolkids_Students_Schoolkids_29_341.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_342.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_344.jpg': (1024, 762),
'29_Students_Schoolkids_Students_Schoolkids_29_349.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_373.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_376.jpg': (1024, 707),
'29_Students_Schoolkids_Students_Schoolkids_29_379.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_381.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_382.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_384.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_385.jpg': (1024, 1024),
'29_Students_Schoolkids_Students_Schoolkids_29_396.jpg': (1024, 528),
'29_Students_Schoolkids_Students_Schoolkids_29_40.jpg': (1024, 732),
'29_Students_Schoolkids_Students_Schoolkids_29_402.jpg': (1024, 468),
'29_Students_Schoolkids_Students_Schoolkids_29_403.jpg': (1024, 555),
'29_Students_Schoolkids_Students_Schoolkids_29_406.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_408.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_413.jpg': (1024, 1579),
'29_Students_Schoolkids_Students_Schoolkids_29_424.jpg': (1024, 682),
'29_Students_Schoolkids_Students_Schoolkids_29_43.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_438.jpg': (1024, 1465),
'29_Students_Schoolkids_Students_Schoolkids_29_442.jpg': (1024, 1583),
'29_Students_Schoolkids_Students_Schoolkids_29_447.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_449.jpg': (1024, 1402),
'29_Students_Schoolkids_Students_Schoolkids_29_452.jpg': (1024, 615),
'29_Students_Schoolkids_Students_Schoolkids_29_469.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_472.jpg': (1024, 680),
'29_Students_Schoolkids_Students_Schoolkids_29_473.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_475.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_478.jpg': (1024, 696),
'29_Students_Schoolkids_Students_Schoolkids_29_479.jpg': (1024, 1054),
'29_Students_Schoolkids_Students_Schoolkids_29_490.jpg': (1024, 1579),
'29_Students_Schoolkids_Students_Schoolkids_29_498.jpg': (1024, 1579),
'29_Students_Schoolkids_Students_Schoolkids_29_5.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_504.jpg': (1024, 629),
'29_Students_Schoolkids_Students_Schoolkids_29_509.jpg': (1024, 1366),
'29_Students_Schoolkids_Students_Schoolkids_29_51.jpg': (1024, 564),
'29_Students_Schoolkids_Students_Schoolkids_29_513.jpg': (1024, 1422),
'29_Students_Schoolkids_Students_Schoolkids_29_517.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_518.jpg': (1024, 664),
'29_Students_Schoolkids_Students_Schoolkids_29_520.jpg': (1024, 576),
'29_Students_Schoolkids_Students_Schoolkids_29_526.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_527.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_531.jpg': (1024, 579),
'29_Students_Schoolkids_Students_Schoolkids_29_535.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_54.jpg': (1024, 560),
'29_Students_Schoolkids_Students_Schoolkids_29_542.jpg': (1024, 765),
'29_Students_Schoolkids_Students_Schoolkids_29_544.jpg': (1024, 1280),
'29_Students_Schoolkids_Students_Schoolkids_29_545.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_547.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_551.jpg': (1024, 1422),
'29_Students_Schoolkids_Students_Schoolkids_29_555.jpg': (1024, 583),
'29_Students_Schoolkids_Students_Schoolkids_29_559.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_561.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_562.jpg': (1024, 1054),
'29_Students_Schoolkids_Students_Schoolkids_29_568.jpg': (1024, 714),
'29_Students_Schoolkids_Students_Schoolkids_29_570.jpg': (1024, 682),
'29_Students_Schoolkids_Students_Schoolkids_29_573.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_578.jpg': (1024, 682),
'29_Students_Schoolkids_Students_Schoolkids_29_579.jpg': (1024, 1346),
'29_Students_Schoolkids_Students_Schoolkids_29_580.jpg': (1024, 713),
'29_Students_Schoolkids_Students_Schoolkids_29_594.jpg': (1024, 521),
'29_Students_Schoolkids_Students_Schoolkids_29_60.jpg': (1024, 727),
'29_Students_Schoolkids_Students_Schoolkids_29_601.jpg': (1024, 1583),
'29_Students_Schoolkids_Students_Schoolkids_29_603.jpg': (1024, 1579),
'29_Students_Schoolkids_Students_Schoolkids_29_604.jpg': (1024, 665),
'29_Students_Schoolkids_Students_Schoolkids_29_606.jpg': (1024, 465),
'29_Students_Schoolkids_Students_Schoolkids_29_615.jpg': (1024, 727),
'29_Students_Schoolkids_Students_Schoolkids_29_63.jpg': (1024, 951),
'29_Students_Schoolkids_Students_Schoolkids_29_630.jpg': (1024, 372),
'29_Students_Schoolkids_Students_Schoolkids_29_633.jpg': (1024, 613),
'29_Students_Schoolkids_Students_Schoolkids_29_639.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_641.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_649.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_655.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_665.jpg': (1024, 372),
'29_Students_Schoolkids_Students_Schoolkids_29_668.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_671.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_673.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_676.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_678.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_68.jpg': (1024, 791),
'29_Students_Schoolkids_Students_Schoolkids_29_693.jpg': (1024, 1366),
'29_Students_Schoolkids_Students_Schoolkids_29_696.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_70.jpg': (1024, 625),
'29_Students_Schoolkids_Students_Schoolkids_29_702.jpg': (1024, 493),
'29_Students_Schoolkids_Students_Schoolkids_29_705.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_709.jpg': (1024, 774),
'29_Students_Schoolkids_Students_Schoolkids_29_714.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_716.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_72.jpg': (1024, 767),
'29_Students_Schoolkids_Students_Schoolkids_29_720.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_725.jpg': (1024, 609),
'29_Students_Schoolkids_Students_Schoolkids_29_732.jpg': (1024, 1345),
'29_Students_Schoolkids_Students_Schoolkids_29_743.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_75.jpg': (1024, 726),
'29_Students_Schoolkids_Students_Schoolkids_29_753.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_759.jpg': (1024, 680),
'29_Students_Schoolkids_Students_Schoolkids_29_772.jpg': (1024, 1178),
'29_Students_Schoolkids_Students_Schoolkids_29_78.jpg': (1024, 684),
'29_Students_Schoolkids_Students_Schoolkids_29_792.jpg': (1024, 633),
'29_Students_Schoolkids_Students_Schoolkids_29_802.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_804.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_807.jpg': (1024, 687),
'29_Students_Schoolkids_Students_Schoolkids_29_814.jpg': (1024, 1449),
'29_Students_Schoolkids_Students_Schoolkids_29_815.jpg': (1024, 2484),
'29_Students_Schoolkids_Students_Schoolkids_29_820.jpg': (1024, 576),
'29_Students_Schoolkids_Students_Schoolkids_29_824.jpg': (1024, 1267),
'29_Students_Schoolkids_Students_Schoolkids_29_831.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_833.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_851.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_854.jpg': (1024, 660),
'29_Students_Schoolkids_Students_Schoolkids_29_863.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_865.jpg': (1024, 616),
'29_Students_Schoolkids_Students_Schoolkids_29_868.jpg': (1024, 1421),
'29_Students_Schoolkids_Students_Schoolkids_29_869.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_874.jpg': (1024, 687),
'29_Students_Schoolkids_Students_Schoolkids_29_876.jpg': (1024, 718),
'29_Students_Schoolkids_Students_Schoolkids_29_88.jpg': (1024, 690),
'29_Students_Schoolkids_Students_Schoolkids_29_883.jpg': (1024, 686),
'29_Students_Schoolkids_Students_Schoolkids_29_885.jpg': (1024, 801),
'29_Students_Schoolkids_Students_Schoolkids_29_89.jpg': (1024, 683),
'29_Students_Schoolkids_Students_Schoolkids_29_894.jpg': (1024, 746),
'29_Students_Schoolkids_Students_Schoolkids_29_899.jpg': (1024, 811),
'29_Students_Schoolkids_Students_Schoolkids_29_909.jpg': (1024, 685),
'29_Students_Schoolkids_Students_Schoolkids_29_911.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_912.jpg': (1024, 1366),
'29_Students_Schoolkids_Students_Schoolkids_29_919.jpg': (1024, 685),
'29_Students_Schoolkids_Students_Schoolkids_29_922.jpg': (1024, 681),
'29_Students_Schoolkids_Students_Schoolkids_29_929.jpg': (1024, 636),
'29_Students_Schoolkids_Students_Schoolkids_29_930.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_934.jpg': (1024, 768),
'29_Students_Schoolkids_Students_Schoolkids_29_94.jpg': (1024, 577),
'29_Students_Schoolkids_Students_Schoolkids_29_940.jpg': (1024, 1324),
'29_Students_Schoolkids_Students_Schoolkids_29_942.jpg': (1024, 767),
'29_Students_Schoolkids_Students_Schoolkids_29_98.jpg': (1024, 683),
}

yolo_labels = convert_to_yolov8(label_file_path, image_sizes)

for label in yolo_labels:
    print(label)
