import unittest
import html_report

if __name__ == '__main__':
    filePath ='Report.html'
    fp = open(filePath,'wb')
    runner = html_report.HTMLTestRunner(
        stream=fp,
        title='{ Test Report }',
        tester='trump.liu'
        
    )
    suite = unittest.defaultTestLoader.discover("./")
    runner.run(suite)