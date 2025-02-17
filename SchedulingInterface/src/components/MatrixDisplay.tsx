import React from 'react';
import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography } from '@mui/material';

interface MatrixDisplayProps {
    matrix: (string | number)[][];
}

const MatrixDisplay: React.FC<MatrixDisplayProps> = ({ matrix }) => {
    if (!matrix || matrix.length === 0) return null;

    const headers = [''].concat(
        Array.from({ length: matrix.length }, (_, i) => 
            i === 0 ? 'α' : i === matrix.length - 1 ? 'ω' : i.toString()
        )
    );

    return (
        <Paper sx={{ margin: 2, padding: 2 }}>
            <Typography variant="h6" gutterBottom>
                Matrice des valeurs
            </Typography>
            <TableContainer>
                <Table size="small">
                    <TableHead>
                        <TableRow>
                            {headers.map((header, index) => (
                                <TableCell key={index} align="center">
                                    {header}
                                </TableCell>
                            ))}
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {matrix.map((row, rowIndex) => (
                            <TableRow key={rowIndex}>
                                <TableCell align="center">
                                    {rowIndex === 0 ? 'α' : rowIndex === matrix.length - 1 ? 'ω' : rowIndex}
                                </TableCell>
                                {row.map((cell, cellIndex) => (
                                    <TableCell key={cellIndex} align="center">
                                        {cell}
                                    </TableCell>
                                ))}
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Paper>
    );
};

export default MatrixDisplay;
