"""
数据检查逻辑类
负责检查QLineEdit的状态，返回状态信息
"""
import re

class CheckLineEdits:
    def __init__(self, line_edits):
        """
        检查所有输入框
        
        Args:
            line_edits (QLineEdit): QLineEdit对象
        """
        
        self.line_edits = line_edits
    
    def is_all_filled(self):
        """
        检查是否所有输入框都已填写
        
        Returns:
            bool: 是否全部填写
        """
        
        for i in self.line_edits:
            text = i.text().strip()
            if len(text) == 0:
                return False
            
            if not self._is_positive_number(text):
                return False
        
        return True
    
    def _is_positive_number(self, text: str):
        """
        检查字符串是否为正数（整数或小数）
        
        Args:
            text: 要检查的字符串
            
        Returns:
            bool: 是否为正数
        """
        # 使用正则表达式检查正数
        # 匹配格式：整数或小数，必须为正数
        # ^       : 字符串开始
        # \d+     : 至少一位数字
        # (\.\d+)?: 可选的小数部分
        # $       : 字符串结束
        pattern = r'^\d+(\.\d+)?$'
        return bool(re.match(pattern, text))
       

class CheckImportFile:
    pass