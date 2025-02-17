import React from 'react';
import { Button } from '@mui/material';
import { PictureAsPdf as PdfIcon } from '@mui/icons-material';
import { jsPDF } from 'jspdf';
import html2canvas from 'html2canvas';
import { GraphData } from '../types/graphTypes';

interface PDFExportProps {
  graphData: GraphData;
  graphRef: React.RefObject<HTMLDivElement>;
  matrixRef: React.RefObject<HTMLDivElement>;
  calendarRef: React.RefObject<HTMLDivElement>;
}

const PDFExport: React.FC<PDFExportProps> = ({ 
  graphData, 
  graphRef, 
  matrixRef, 
  calendarRef 
}) => {
  const exportToPDF = async () => {
    const pdf = new jsPDF('p', 'mm', 'a4');
    const margin = 10;
    let yOffset = margin;

    // Add title
    pdf.setFontSize(20);
    pdf.text('Graph Scheduling Analysis Report', margin, yOffset);
    yOffset += 15;

    // Add basic information
    pdf.setFontSize(12);
    pdf.text(`Generated on: ${new Date().toLocaleString()}`, margin, yOffset);
    yOffset += 10;
    pdf.text(`Number of tasks: ${graphData.tasks.length}`, margin, yOffset);
    yOffset += 10;
    pdf.text(`Circuit detected: ${graphData.hasCircuit ? 'Yes' : 'No'}`, margin, yOffset);
    yOffset += 15;

    // Add graph visualization
    if (graphRef.current) {
      const graphCanvas = await html2canvas(graphRef.current);
      const graphImgData = graphCanvas.toDataURL('image/png');
      pdf.addImage(graphImgData, 'PNG', margin, yOffset, 190, 100);
      yOffset += 110;
    }

    // Add matrix
    if (matrixRef.current) {
      const matrixCanvas = await html2canvas(matrixRef.current);
      const matrixImgData = matrixCanvas.toDataURL('image/png');
      pdf.addPage();
      yOffset = margin;
      pdf.text('Value Matrix', margin, yOffset);
      yOffset += 10;
      pdf.addImage(matrixImgData, 'PNG', margin, yOffset, 190, 100);
      yOffset += 110;
    }

    // Add calendar
    if (calendarRef.current) {
      const calendarCanvas = await html2canvas(calendarRef.current);
      const calendarImgData = calendarCanvas.toDataURL('image/png');
      pdf.addPage();
      yOffset = margin;
      pdf.text('Calendar and Margins', margin, yOffset);
      yOffset += 10;
      pdf.addImage(calendarImgData, 'PNG', margin, yOffset, 190, 100);
    }

    // Save the PDF
    pdf.save('graph-scheduling-report.pdf');
  };

  return (
    <Button
      variant="contained"
      color="primary"
      startIcon={<PdfIcon />}
      onClick={exportToPDF}
      sx={{ mt: 2 }}
    >
      Export to PDF
    </Button>
  );
};

export default PDFExport;
