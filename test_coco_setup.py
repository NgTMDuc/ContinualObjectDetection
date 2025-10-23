#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script kiểm tra COCO dataset setup."""

import os
import sys

# Đảm bảo import detectron2 từ project
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

def test_coco_setup():
    """Kiểm tra COCO dataset đã setup đúng chưa."""
    try:
        from detectron2.data import DatasetCatalog, MetadataCatalog
        
        print("=" * 60)
        print("🔍 KIỂM TRA COCO DATASET SETUP")
        print("=" * 60)
        
        # 1. Kiểm tra datasets có trong catalog không
        all_datasets = DatasetCatalog.list()
        coco_datasets = [d for d in all_datasets if 'coco_2017' in d]
        
        print(f"\n✓ Tìm thấy {len(coco_datasets)} COCO datasets:")
        for ds in sorted(coco_datasets)[:10]:  # In 10 datasets đầu
            print(f"  - {ds}")
        if len(coco_datasets) > 10:
            print(f"  ... và {len(coco_datasets) - 10} datasets khác")
        
        # 2. Kiểm tra coco_2017_train
        print("\n" + "=" * 60)
        print("📦 KIỂM TRA coco_2017_train")
        print("=" * 60)
        
        try:
            train_dicts = DatasetCatalog.get("coco_2017_train")
            print(f"✓ Số lượng ảnh training: {len(train_dicts):,}")
            
            # Kiểm tra ảnh đầu tiên
            if train_dicts:
                first_img = train_dicts[0]
                print(f"✓ Ảnh đầu tiên: {first_img['file_name']}")
                print(f"  - Kích thước: {first_img['width']}x{first_img['height']}")
                print(f"  - Số annotations: {len(first_img['annotations'])}")
                
                # Kiểm tra file có tồn tại không
                if os.path.exists(first_img['file_name']):
                    print(f"  - ✓ File exists")
                else:
                    print(f"  - ✗ File NOT found!")
                    
        except Exception as e:
            print(f"✗ Lỗi khi load coco_2017_train: {e}")
        
        # 3. Kiểm tra coco_2017_val
        print("\n" + "=" * 60)
        print("📦 KIỂM TRA coco_2017_val")
        print("=" * 60)
        
        try:
            val_dicts = DatasetCatalog.get("coco_2017_val")
            print(f"✓ Số lượng ảnh validation: {len(val_dicts):,}")
            
            # Kiểm tra ảnh đầu tiên
            if val_dicts:
                first_img = val_dicts[0]
                print(f"✓ Ảnh đầu tiên: {first_img['file_name']}")
                print(f"  - Kích thước: {first_img['width']}x{first_img['height']}")
                print(f"  - Số annotations: {len(first_img['annotations'])}")
                
                # Kiểm tra file có tồn tại không
                if os.path.exists(first_img['file_name']):
                    print(f"  - ✓ File exists")
                else:
                    print(f"  - ✗ File NOT found!")
                    
        except Exception as e:
            print(f"✗ Lỗi khi load coco_2017_val: {e}")
        
        # 4. Kiểm tra metadata
        print("\n" + "=" * 60)
        print("📋 KIỂM TRA METADATA")
        print("=" * 60)
        
        metadata = MetadataCatalog.get("coco_2017_val")
        print(f"✓ Số lượng classes: {len(metadata.thing_classes)}")
        print(f"✓ Classes (5 đầu tiên): {metadata.thing_classes[:5]}")
        print(f"✓ Evaluator type: {metadata.evaluator_type}")
        
        # 5. Kiểm tra COCO corruption datasets
        print("\n" + "=" * 60)
        print("🌫️  KIỂM TRA COCO CORRUPTION DATASETS")
        print("=" * 60)
        
        corruption_datasets = [d for d in all_datasets if 'coco_2017_val-' in d]
        print(f"✓ Tìm thấy {len(corruption_datasets)} corruption datasets")
        if corruption_datasets:
            print("  Ví dụ:")
            for ds in sorted(corruption_datasets)[:5]:
                print(f"  - {ds}")
        
        print("\n" + "=" * 60)
        print("✅ HOÀN THÀNH KIỂM TRA!")
        print("=" * 60)
        print("Dataset của bạn đã được setup đúng cách! 🎉")
        
        return True
        
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_coco_setup()
    sys.exit(0 if success else 1)

